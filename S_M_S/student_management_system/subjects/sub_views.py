
from urllib import response

from django.shortcuts import get_object_or_404
from ..models.semester_models import SemesterModel
from ..models.subjects_models import SubjectsModel
from ..subjects.sub_serializers import SubjectSerializers
from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.exceptions import ValidationError 


class SubjectAPIView(generics.GenericAPIView):
    queryset = SubjectsModel.objects.all()
    serializer_class = SubjectSerializers
    permission_classes = [AllowAny]
    parser_classes = [JSONParser]


    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data= request.data)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=201)
        except ValidationError as e:
            return Response(
                {"error": "Invalid data", "details": e.detail},
                status=400
            )
        except Exception as e:
            return Response(
                {"error": "Something went wrong", "details": str(e)},
                status=500
            )


    def get(self, request, *args, **kwargs):
        subject_data = self.get_queryset()

        if not subject_data.exists():
            return Response(
                 {"message": "No data found"},
                    status=status.HTTP_200_OK
            )
        
        serializer = SubjectSerializers(subject_data, many = True)
        return Response(
             {
                    "count": subject_data.count(),
                    "courses": serializer.data
                },
                status=status.HTTP_200_OK
        )
        




class SingleSubjectApiView(generics.GenericAPIView):
    serializer_class = SubjectSerializers
    permission_classes = [AllowAny]

    parser_classes = [JSONParser]

    def get(self, request,pk, *args, **kwargs):
        
            subject_data = get_object_or_404(SubjectsModel,pk=pk)  # NoteDont need to use try except when we use get_object_or_404 it handles itself
            serializer = SubjectSerializers(subject_data)
            return Response(
                {
                     "message":"Subject data fetched sucessfully",
                      "data":serializer.data
                },
                
                     status=status.HTTP_200_OK
            )

    def put(self, request, pk, *args, **kwargs):
         
         subject_data = get_object_or_404(SubjectsModel, pk=pk)
         
         serializer = SubjectSerializers(subject_data,data = request.data)

         if serializer.is_valid():
              serializer.save()
              return Response(
                     {'message':'Subject data updated sucessfully'}, status=status.HTTP_201_CREATED
                )
         return Response(
            {"error": "Something went wrong!"}, status=status.HTTP_400_BAD_REQUEST
               )

         
    def delete(self, request, pk, *args, **kwargs):
         try:
         
            subject = get_object_or_404(SubjectsModel, pk=pk)
            subject.delete()
            return Response( {"success": f"Subject with id {pk} deleted successfully"},
            status=status.HTTP_200_OK)
         except SubjectsModel.DoesNotExist:
              return Response(
                   {
                        "error": f"Subject with id {pk} not found"
                   },
                   status=status.HTTP_404_NOT_FOUND


              )
              


         
            



