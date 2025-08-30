# from rest_framework.decorators import api_view
# 
# import re
from urllib import request, response
from rest_framework import status

# from api.serializers.student_serializers import studentSerializer


from rest_framework.decorators import api_view
from rest_framework.response import Response

from api import serializers
from ..serializers.student_serializers import studentSerializer 
from ..models.studentmodel import student
from rest_framework.response import Response

from ..models.studentmodel import student
# from api.models import studentmodel




# from apiproject.models import studentmodel   for another full approach 


@api_view(['GET','POST'])
def Studentview(request):

    if request.method == 'GET':
        students_data = student.objects.all()
        serializer = studentSerializer(students_data, many=True )
   
        return Response(
            serializer.data, status= status.HTTP_200_OK
            )

    elif request.method == 'POST':
        serializer = studentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(
                serializer.data, status= status.HTTP_201_CREATED,

            )
        else:
            return Response(
                status.HTTP_400_BAD_REQUEST, status.HTTP_401_UNAUTHORIZED
            )


# To manipulate a details of a single user

@api_view(['GET', 'DELETE', 'PUT'])
def StudentDetailView(request, pk):
    try:
        student_data = student.objects.get(pk=pk)
      
    except student.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        # pk is primary key and that holds student id
        serializer = studentSerializer(student_data)
        return Response(serializer.data, status.HTTP_200_OK)
    
    elif request.method == 'DELETE':
                 student_data.delete()
                 return Response(status.HTTP_200_OK)
    
    elif request.method == 'PUT':
             # to manipulate single student id pk = primary key, stident id is primary
        serializer = studentSerializer(student_data,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
