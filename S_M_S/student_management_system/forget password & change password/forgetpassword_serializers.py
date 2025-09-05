import email
from ..models.user_models import UserModel
from rest_framework import serializers

class PasswordResetSerializers(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self,value):
        if not UserModel.objects.filter(email=value).exists():
            raise serializers.ValidationError("No user with this email found.")
        
        return value   # return value return the email if user does exist in database
    


class ChangePasswordSerializer(serializers.Serializer):
    pass
