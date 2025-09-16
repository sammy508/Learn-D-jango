import email
from os import error
import token
from typing import Required
from xmlrpc.client import ResponseError
from ...models.user_models import UserModel
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import smart_str, force_bytes,force_str
from django.utils.http  import urlsafe_base64_encode, urlsafe_base64_decode
import time
from django.core.mail import send_mail,BadHeaderError
from rest_framework import status
from rest_framework.response import Response
from django.conf import settings
import smtplib


class PasswordresetManager:
    """
    Handles all password reset related tasks:
    1. Generate token
    2. Build reset link
    3. Send email
    4. Validate token (optional)
    """
       


    def __init__(self, user, link_url ="http://localhost:8000/reset-password/"):
        self.user = user
        self.link_url = link_url 

    def generate_token(self):
        """
        Generate a combined token: <uidb64>.<token>.<timestamp>
        """
        uidb64 = urlsafe_base64_encode(force_bytes(self.user.pk))
        token = default_token_generator.make_token(self.user)
        ts = str(int(time.time()))
        return f"{uidb64}.{token}.{ts}"
    


    def build_reset_link(self):
        """
        Build a clickable URL for the email.
        """

        token = self.generate_token()
        return f"{self.link_url}{token}/"

    


    def send_email(self, subject=None, message=None):

        """
        Send password reset token to user via email.
        """
        reset_link = self.build_reset_link()
        if subject is None:
            subject = "Reset Your fkin password"
        
        if message is None:

            message = (
                f"Hi{self.user.USERNAME_FIELD},\n\n"
                f"Click the link below to reset your password:\n{reset_link}\n\n"
                f" This link will expire in 30 min"

            )

        send_mail(
            subject, message, settings.DEFAULT_FROM_EMAIL, [self.user.email], fail_silently=False

        )

        return reset_link
    
    @staticmethod

    def validate_token(user, token, expiry_second = 1800):
        " validates token and checks expiry of link"

        try:
            uidb64, realtoken, ts = token.split(".")

            uid = force_str(urlsafe_base64_decode(uidb64))

            if str(user.pk)!= uid:
                return False
            
            if time.time() - int(ts):  # subtracting created time frm current time
                return Response({"message": "Password reset link sent."}, status=status.HTTP_200_OK)


        
            if not default_token_generator.check_token(user, realtoken):
                return False


        except BadHeaderError:
            return {"success": False, "error": "Invalid email header."}

        except smtplib.SMTPException as e:
            return {"success": False, "error": str(e)}

        except Exception as e:
            return {"success": False, "error": f"Unexpected error: {e}"}
        




