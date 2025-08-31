

from django.shortcuts import get_object_or_404
from ..models.user_models import UserModel
from ..serializers.User_serializer import Userserializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class UserCreateApiView(APIView):

    def post(self, request):

        try:

            if request.user.roles.lower() != 'admin':
                return Response(
                    {"error": "Only admin can create users"}, status= status.HTTP_403_FORBIDDEN
                )
            
            else:
                serializer = Userserializer(data = request.data)
                if serializer.is_valid():
                    serializer.save() 
                    return Response(
                        {"message": "User created successfully"}, 
                        status= status.HTTP_201_CREATED
                )
        
        except :
            return Response(
                serializer.errors,
                status= status.HTTP_400_BAD_REQUEST,
            )

  