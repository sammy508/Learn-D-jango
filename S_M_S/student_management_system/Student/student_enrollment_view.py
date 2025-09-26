
from urllib import response

from django.shortcuts import get_object_or_404
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
            serializer.is_valid()
            serializer.save()
            return Response(
                 {"message":"Enrollment record Created Sucessfully"},
                serializer.data, status=201
            )

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


    def get(self,request,*args,**kwargs):
        try:
            enrollment_data = self.get_queryset()

            if not enrollment_data.exists():
                return Response(

                    serializer.data,
                    status=status.HTTP_200_OK
                )
            serializer = StudentEnrollmentSerializer(instance=enrollment_data, many=True)
        except Exception as e : 
            return Response({"error": "Something went wrong", "details": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            

class SingleSrudentView(generics.GenericAPIView):
    permission_classes = [AllowAny]   # have to change later
    serializer_class = StudentEnrollmentSerializer


    def get(self,pk,request,*args,**kwargs):

        enrollment_data = get_object_or_404(StudentEnrollmentModel, pk=pk)
        serializer = StudentEnrollmentSerializer(enrollment_data)

        return Response(
            {
                "message":"Enrollmentdata fetched sucessfully",
                "data":serializer.data
            },
            status=status.HTTP_200_OK
        )
    

    def put(self,pk,request,*args,**kwargs):
        enroll_data = get_object_or_404(StudentEnrollmentModel, pk=pk)
        serializer = StudentEnrollmentSerializer(data=request.data)

        pass

    def delete(self,pk,request,*args,**kwargs):
        pass