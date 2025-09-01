

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
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        password = serializer.validated_data['password']  # Change from usr_password to password

        try:
            user = UserModel.objects.get(email=email)
            if user.check_password(password):  # And here too
                refresh = RefreshToken.for_user(user)
                return Response({
                    "message": "Login successful",
                    "user": {
                        "id": str(user.id),  # Make sure to convert UUID to string
                        "email": user.email,
                        "role": user.role,
                        "is_staff": user.is_staff,
                        "is_active": user.is_active,
                    },
                    "tokens": {
                        "refresh": str(refresh),
                        "access": str(refresh.access_token),
                    }
                }, status=status.HTTP_200_OK)
            else:
                return Response(
                    {'message': 'Invalid password'},
                    status=status.HTTP_401_UNAUTHORIZED
                )
                
        except UserModel.DoesNotExist:
            return Response(
                {'message': 'User with this email does not exist'},
                status=status.HTTP_401_UNAUTHORIZED
            )
        except Exception as e:
            return Response(
                {'message': f'Login error: {str(e)}'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )