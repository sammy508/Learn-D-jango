
from signal import valid_signals
from urllib import response

from django.shortcuts import get_object_or_404
from yaml import serialize
from ..models.semester_models import SemesterModel
from ..models.subjects_models import SubjectsModel

from rest_framework.views import APIView
from ..models.student_class_models import StudentClassModel
from .student_calss_serializers import StudentClassSerializers

from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, AllowAny,IsAdminUser
from rest_framework.exceptions import ValidationError 


class StudentClassView(generics.GenericAPIView):
    queryset = StudentClassModel.objects.all()
    serializer_class = StudentClassSerializers
    permission_classes = [AllowAny]

    def post(self,request,*args,**kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception = True)
            serializer.save()
            return Response(
                 {"message":"StudentClass is created Sucessfully",
                  "data":serializer.data},
                  status= status.HTTP_201_CREATED

            )
        except ValidationError as e :
              return Response(
                {"error": "Invalid data", "details": e.detail},
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            return Response(
                {"error": "Something went wrong", "details": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        
    def get(self,request,*args,**kwargs):
        try:
            student_calss_data = self.get_queryset()

            if not student_calss_data.exists():
                return Response(
                    {"message":"Student class record not found","data": []},
                    status= status.HTTP_400_BAD_REQUEST
                )
            serializer = StudentClassSerializers(student_calss_data, many=True)
            return Response(
                  {
                    "message": "Studentclass records fetched successfully",
                    "data": serializer.data
                },
                status= status.HTTP_200_OK
            )

        except Exception as e : 
             return Response({"error": "Something went wrong", "details": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            


class SingleStudentClassView(generics.GenericAPIView):
    queryset = StudentClassModel.objects.all()
    serializer_class = StudentClassSerializers
    permission_classes = [AllowAny]


    def get(self,request,pk,*args,**kwargs):
        try:
            student_calss_data = get_object_or_404(StudentClassModel,pk=pk)

          
            serilazer = StudentClassSerializers(student_calss_data)
            return Response(
                  {
                    "message": "Studentclass records fetched successfully",
                    "data": serilazer.data
                },
                status= status.HTTP_200_OK
            )

        except Exception as e : 
             return Response({"error": "Something went wrong", "details": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
    def put(self,request,pk,*args,**kwargs):
        student_class_data = get_object_or_404(StudentClassModel, pk=pk)
        serializer = StudentClassSerializers(student_class_data, data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
        except ValidationError as e:
            return Response(
                {"messgae":"Invalid data", "details":e.detail},status= status.HTTP_400_BAD_REQUEST
            )
        

    def delete(self,request,pk,*args,**kwargs):
        try:
            student_class_data = get_object_or_404(StudentClassModel,pk=pk)
            student_class_data.delete()
        except :
            return Response(
                {"error":"Student_class deleted Suxessfully"},
                status=status.HTTP_404_NOT_FOUND
            )
