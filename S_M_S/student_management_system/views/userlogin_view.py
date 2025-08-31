

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
        print("Login request received:", request.data)
        
        serializer = self.get_serializer(data=request.data)
        
        if not serializer.is_valid():
            print("Serializer errors:", serializer.errors)
            return Response(
                {'message': 'Invalid input data', 'errors': serializer.errors},
                status=status.HTTP_400_BAD_REQUEST
            )

        email = serializer.validated_data['email']
        password = serializer.validated_data['password']  # FIXED: Changed from 'usr_password' to 'password'
        
        print(f"Attempting login for: {email}")

        try:
            # Check if user exists
            user = UserModel.objects.get(email=email)
            print(f"User found: {user.email}")
            print(f"Stored password hash: {user.password}")
            
            # Check password
            password_valid = user.check_password(password)
            print(f"Password check result: {password_valid}")
            
            if password_valid:
                # Generate JWT tokens
                refresh = RefreshToken.for_user(user)
                print("Login successful, tokens generated")
                
                return Response({
                    "message": "Login successful",
                    "user": {
                        "id": user.id,
                        "email": user.email,
                        "username": user.username,
                        "roles": user.roles,  # Added roles to response
                    },
                    "tokens": {
                        "refresh": str(refresh),
                        "access": str(refresh.access_token),
                    }
                }, status=status.HTTP_200_OK)
            else:
                print("Invalid password")
                return Response(
                    {'message': 'Invalid password'},
                    status=status.HTTP_401_UNAUTHORIZED
                )
                
        except UserModel.DoesNotExist:
            print("User not found")
            return Response(
                {'message': 'User not found'},
                status=status.HTTP_401_UNAUTHORIZED
            )
        except Exception as e:
            print(f"Unexpected error: {str(e)}")
            import traceback
            traceback.print_exc()
            return Response(
                {'message': 'Authentication failed'},
                status=status.HTTP_401_UNAUTHORIZED
            )


# class UserloginApiView(generics.GenericAPIView):
#     serializer_class = UserLoginSerializer


#     def post(self, request, *args, **kwargs):
#         serializer= self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         email = serializer.validated_data['email']
#         usr_password  = serializer.validated_data['usr_password']

#         user = authenticate(request, email=email, password=usr_password)
        



#         try:
#             user = UserModel.objects.get(email=email)
#             if user.check_password(usr_password):
#                 refresh = RefreshToken.for_user(user)
#                 return Response({
#                     "message": "Login successful",
#                     "user": {
#                         "id": user.id,
#                         "email": user.email,
#                         "username": user.username,  # or "roles"
#                     },
#                     "tokens": {
#                         "refresh": str(refresh),
#                         "access": str(refresh.access_token),
#                     }
#                 }, status=status.HTTP_200_OK)
#         except :
#                 return Response(
#                     {'message': 'Invalid credentials babe put correct one'},
#                     status=status.HTTP_401_UNAUTHORIZED
#                 )

        







    