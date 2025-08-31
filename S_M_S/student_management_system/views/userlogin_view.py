from logging import raiseExceptions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from django.contrib.auth import authenticate
from rest_framework import serializers
from ..models.user_models import UserModel  # Import your custom UserModel
from typing import Dict, Any
from ..serializers.login_serializer import UserLoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken

from ..serializers.login_serializer import UserLoginSerializer
from django.contrib.auth.hashers import check_password
from rest_framework.exceptions import AuthenticationFailed




class UserloginApiView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer


    def post(self, request, *args, **kwargs):
        serializer= self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        password = serializer.validated_data['usr_password']


        user = authenticate(request, username=email, password=password)
        user = authenticate(request, username=email, password=password)



        try:
            user = UserModel.objects.get(email=email)
       

            if user is not None:
                refresh = RefreshToken.for_user(user)

                return Response({
                    "message": "Login successful",
                    "user": {
                        "id": user.id,
                        "email": user.email,
                        "username": user.username,  # or "roles"
                    },
                    "tokens": {
                        "refresh": str(refresh),
                        "access": str(refresh.access_token),
                    }
                }, status=status.HTTP_200_OK)
        except :
                return Response(
                    {'message': 'Invalid credentials babe put correct one'},
                    status=status.HTTP_401_UNAUTHORIZED
                )

        
        






    