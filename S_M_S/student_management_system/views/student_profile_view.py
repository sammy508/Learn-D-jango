

from ast import Delete
from functools import partial
import profile
from django.shortcuts import get_object_or_404
from yaml import serialize


from ..serializers.student_profile_serializers import StudentProfileSerializer
from ..models.student_models import StudentModel

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class  StudentApiview(APIView):

    def get(self,request,pk=None):

        try:
            if pk:
                student_data = get_object_or_404(StudentModel, pk=pk)
                serializer = StudentProfileSerializer(student_data,many=True)

                return Response(
                    serializer.data, status= status.HTTP_200_OK 
                )
            else:
                student_data = StudentModel.objects.all()
                serializer = StudentProfileSerializer(student_data,many=True)

                return Response(
                    serializer.data, status= status.HTTP_200_OK 
                )


        except StudentModel.DoesNotExist:
            return Response(
                status=status.HTTP_404_NOT_FOUND
            )
        


    def post(self, request, *args, **kwargs):

        serializer = StudentProfileSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(  serializer.data, status = status.HTTP_201_CREATED)

        return Response({"error": "Something went wrong!"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

    def put(self, request, pk, *args, **kwargs):
        student_data = get_object_or_404(StudentModel, pk=pk)
        serializer= StudentProfileSerializer(student_data,data = request.data,partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data, status = status.HTTP_201_CREATED
            )
        return Response(
            {"error": "Something went wrong!"}, status=status.HTTP_400_BAD_REQUEST
        )
    

    def delete(self, request, *args, **kwargs):
        student_data = get_object_or_404(StudentModel, user=request.user )
        student_data.delete_avatar()

       



        
    