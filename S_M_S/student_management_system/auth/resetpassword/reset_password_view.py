
import email
from multiprocessing import managers
from pickle import TRUE
import token
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from yaml import serialize



from ...models.user_models import UserModel
from django.contrib.auth.tokens import default_token_generator
from rest_framework.generics import GenericAPIView
from ..resetpassword.reset_password_serializer import ResetPasswordSerializer, SendresetLinkSerializer
from ..utils.reset_password import PasswordresetManager
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




















# class ResetPasswordView(generics.UpdateAPIView):
#     serializer_class = ChangePasswordSerializer
#     permission_classes = [AllowAny] 

#     def get_object(self):
#         return self.request.user
    
    
    
#     def post(self,request, *args, **kwargs):
#         serializer = PasswordResetSerializers(data = request.data)
#         serializer.is_valid(raise_exception=True)

#         email = serializer.validated_data['email']
#         user = UserModel.objects.get(email = email)


#         # create a token 

#         token = default_token_generator.make_token(user)
#         reset_url = f"http://127.0.0.1:8000/api/v1/resetpassword/?user_id={user.pk}&token={token}"

#         return Response({
#         "reset_url": reset_url,
#         "message": "Use this URL to reset your password (backend-only)"
#     }, status=200)

    







