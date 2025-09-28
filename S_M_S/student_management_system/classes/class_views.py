

from urllib import response

from django.shortcuts import get_object_or_404
from yaml import serialize
from ..models.semester_models import SemesterModel
from ..models.subjects_models import SubjectsModel
from ..models.class_model import ClassModel
from rest_framework.views import APIView
from .class_serializers import ClassSerializers

from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, AllowAny,IsAdminUser
from rest_framework.exceptions import ValidationError 


class ClassView(generics.GenericAPIView):
    queryset = ClassModel.objects.all()
    serializer_class = ClassSerializers
    permission_classes = [AllowAny]  


    def post(self,request,*args,**kwargs):
        serializer = self.get_serializer(data = request.data)

        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(
                 {"message":"Class record Created Sucessfully",
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
