
import email
from multiprocessing import managers
from pickle import TRUE
import re
import token
from rest_framework import generics, status, permissions
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from yaml import serialize



from ...models.user_models import UserModel
from django.contrib.auth.tokens import default_token_generator
from rest_framework.generics import GenericAPIView
from ..resetpassword.reset_password_serializer import ResetPasswordSerializer, SendresetLinkSerializer, ChangePasswordSerializer
from ..utils.reset_password import  PasswordresetManager
from django.contrib.auth import get_user_model
from .model.password_reset_model import PasswordReset

User = get_user_model()

class SendResetPasswordLinkView(generics.GenericAPIView):

    """hit post method to enter email to get reset link"""

    serializer_class = SendresetLinkSerializer


    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception = True)

        email = serializer.validated_data['email']
        user = User.objects.filter(email=email).first()
           
        if not user:
            return Response(
                {"error": "User not found."}, status=status.HTTP_404_NOT_FOUND
            )
        
        manager = PasswordresetManager(user)
        manager.send_email()


        if not result['success']:
            return Response(
                result, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


        return Response({"message": "Password reset link sent."}, status=status.HTTP_200_OK)



class ResetPaswordView(generics.GenericAPIView):
    serializer_class = ResetPasswordSerializer
    permission_classes = [AllowAny]

    def post(self, request, token, *args, **kwargs):

        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception=True)

        # safe extraction of the data
        data = serializer.validated_data
        new_password = data.get("new_password")
        confirm_password = data.get("confirm_password")

        if new_password != confirm_password:
            return Response(
                {"error": "Passwords do not match"}, status=400
            )
        
        reset_obj = PasswordReset.objects.filter(token = token).first()

        if not reset_obj:
            return REsponse(
                {'error':'Invalid token'}, status =status.HTTP_400_BAD_REQUEST
            )
        
        user = UserModel.objects.filter(email=reset_obj.email).first()

        if user:
            user.set_password(request.data['new_passsword'])
            user.save()

            reset_obj.delete()

            return Response(
                {'message':"Paswword updated sucessfully"}
            )
        return Response(
            {'error':'No user found'}, status=404
        )




class ChangepasswordView(generics.GenericAPIView):
    serializer_class = ChangePasswordSerializer
    model = UserModel
    permission_classes = [permissions.IsAuthenticated]

   
    
    def put(self,request, *args, **kwargs):

        user = request.user  # logged-in user, no need for pk/id it end the necessicity of PK
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

    

        old_password = serializer.validated_data['old_password'] 
        new_password = serializer.validated_data['new_password']
        confirm_password = serializer.validated_data['confirm_password'] 

        if not  user.check_password(old_password):
            return Response(
                {"error": "Old password does not match"}, status=status.HTTP_400_BAD_REQUEST
            )
        
        user.set_password(new_password)
        user.save()


        return Response(
            {"success": "Password changed successfully."}, status=200
        )
    

        
        









