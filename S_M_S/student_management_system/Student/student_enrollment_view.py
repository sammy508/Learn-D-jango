
from urllib import response

from django.shortcuts import get_object_or_404
from yaml import serialize
from ..models.semester_models import SemesterModel
from ..models.subjects_models import SubjectsModel
from ..models.student_enrollment_models import StudentEnrollmentModel
from rest_framework.views import APIView
from ..Student.student_enrollment_serializer import StudentEnrollmentSerializer

from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, AllowAny,IsAdminUser
from rest_framework.exceptions import ValidationError 



class StudentEnrollView(generics.GenericAPIView):
    queryset = StudentEnrollmentModel.objects.all()
    serializer_class = StudentEnrollmentSerializer
    permission_classes = [AllowAny]    # Have to update later 

    def post(self,request,*args,**kwargs):
        serializer = self.get_serializer(data = request.data)

        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(
                 {"message":"Enrollment record Created Sucessfully",
                  "data": serializer.data
                 },
                status= status.HTTP_201_CREATED
            )

        except ValidationError as e:
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
            enrollment_data = self.get_queryset()

            if not enrollment_data.exists():
                return Response({
                      "message": "No enrollment records found",
            "data": []
                },
                status=status.HTTP_200_OK

                   
                )
            serializer = StudentEnrollmentSerializer(instance=enrollment_data, many=True)
            return Response(
                {
                    "message": "Enrollment records fetched successfully",
                    "data": serializer.data
                },
                status= status.HTTP_200_OK

            )
        except Exception as e : 
            return Response({"error": "Something went wrong", "details": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            

class SingleStudentEnrollView(generics.GenericAPIView):
    permission_classes = [AllowAny]   # have to change later
    serializer_class = StudentEnrollmentSerializer


    def get(self,request,pk,*args,**kwargs):

        enrollment_data = get_object_or_404(StudentEnrollmentModel, pk=pk)
        serializer = StudentEnrollmentSerializer(enrollment_data)

        return Response(
            {
                "message":"Enrollmentdata fetched sucessfully",
                "data":serializer.data
            },
            status=status.HTTP_200_OK
        )
    

    def put(self,request,pk,*args,**kwargs):
        enroll_data = get_object_or_404(StudentEnrollmentModel, pk=pk)
        serializer = StudentEnrollmentSerializer(enroll_data,data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(
                {"message":"Enrollment data updated sucessfully"},
                status= status.HTTP_201_CREATED

            )
        except ValidationError as e : 
            return Response(
                 {"error": "Invalid data", "details": e.detail},
                status=status.HTTP_400_BAD_REQUEST

            )



        

    def delete(self,request,pk,*args,**kwargs):
       try:
           enroll_data = get_object_or_404(StudentEnrollmentModel,pk=pk)
           enroll_data.delete()
           return Response(
                {"message": "Student deleted successfully"}, 
                status=status.HTTP_204_NO_CONTENT
            )

       except:
           return  Response(
                {"error": "Student not found"}, 
                status=status.HTTP_404_NOT_FOUND

            )
