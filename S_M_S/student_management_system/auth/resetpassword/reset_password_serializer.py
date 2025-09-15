from typing import Required
from wsgiref import validate
from rest_framework import serializers
import re


class SendresetLinkSerializer(serializers.Serializer):
    email = serializers.EmailField()


# After clicking link and we have to work on reset new password

  
class ResetPasswordSerializer(serializers.Serializer):
    new_password = serializers.RegexField(
        regex=r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$',
        write_only=True,
        error_messages={'invalid': ('Password must be at least 8 characters long with at least one capital letter and symbol')})
    confirm_password = serializers.CharField(write_only=True, required=True)

    def validate(self, data):
        if data['new_password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match.")
        
        return data     # else returns data

class ChangePasswordSerializer(serializers.Serializer):
   

    old_password = serializers.CharField(required= True)
    new_password = serializers.CharField(required= True, min_length = 8)
    confirm_password = serializers.CharField(required= True, min_length = 8)

    def validate_password (self, value):
        """
        Validate password strength using regex
        Example: At least 1 uppercase, 1 lowercase, 1 digit, 1 special char
        """
        
        regex=r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'

        if not re.match(regex, value):
            raise serializers.ValidationError(
                    "Password must contain at least 8 characters, including "
                "one uppercase letter, one lowercase letter, one number, and one special character."
            )
        return value
    
    def validate(self, data):
      
      if data['new_password'] != data['confirm_password']:
          raise serializers.ValidationError(
              "New passwords do not match."
          )


      return data

        