
from rest_framework import serializers
from ..models.user_models import UserModel

class UserLoginSerializer(serializers.Serializer):

    email = serializers.EmailField()
    usr_password = serializers.CharField(write_only=True)