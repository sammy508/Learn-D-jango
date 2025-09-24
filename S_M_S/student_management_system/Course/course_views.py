

from ast import Delete
from asyncio.windows_events import NULL
from functools import partial
from multiprocessing import reduction
from os import stat
import profile
from urllib import response
from webbrowser import get
from django.shortcuts import get_object_or_404
from yaml import serialize



from ..Course.course_serializers import CourseSerializer
from ..Course.course_model import CourseModel
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.pagination import PageNumberPagination



class CourseApiView(APIView):
    parser_classes = [MultiPartParser, FormParser]
  

    def get(self,*args,**kwargs):

            course_data = CourseModel.objects.all()

            if not course_data.exists():  # call .exists() as a method
                return Response(
                    {"message": "No data found"},
                    status=status.HTTP_200_OK
                )

            # Pass the queryset as instance, not data=
            serializer = CourseSerializer(course_data, many=True)
            return Response(
                {
                    "count": course_data.count(),
                    "courses": serializer.data
                },
                status=status.HTTP_200_OK
            )

            
        
        
           
    
    def post(self, request, *args, **kwargs):
        
           serializer = CourseSerializer(data = request.data)
           if serializer.is_valid():
             serializer.save()
             return Response(
                serializer.data, status= status.HTTP_201_CREATED
             )
           return Response( 
            
               status=status.HTTP_400_BAD_REQUEST,
           )

            
       
class CourseSingalApiView(APIView):
        parser_classes = [MultiPartParser, FormParser]
      
        def put(self,request,pk,*args,**kwargs):
           course = get_object_or_404(CourseModel, pk=pk)
           serializer = CourseSerializer(data =request.data)
           if serializer.is_valid():
                serializer.save()
                return Response(
                     {'message':'Course data updated sucessfully'}
                )
           return Response(
            {"error": "Something went wrong!"}, status=status.HTTP_400_BAD_REQUEST
               )


        def get(self,request,pk,*args,**kwargs):
            # pk = kwargs.get('pk')   if we  have to pass request, as 2nd parameterin method or we have to inject pk using kwargs
            try:
                course_data = get_object_or_404(CourseModel, pk=pk)
                serializer = CourseSerializer(course_data)
                return Response(
                     serializer.data,
                     status=status.HTTP_200_OK
                )

      
           
            except CourseModel.DoesNotExist:
                
                return Response(
                    {"error": "Student not found"}, 
                    status=status.HTTP_404_NOT_FOUND
                )

        def delete(self,request,pk,*args,**kwargs):
             
             try:
                course = CourseModel.objects.get(pk=pk)
                course.delete()
        
                return Response(
                     {'message':'Course deleted sucessfully'},
                     status= status.HTTP_200_OK

                )
             except CourseModel.DoesNotExist:
                  return Response(
                       {'message':'Course is not found'},
                       status=status.HTTP_404_NOT_FOUND
                  )
      


# // Have to update course post then make a seperate view for specific course part put, get, delete request