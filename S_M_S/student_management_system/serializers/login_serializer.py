
from rest_framework import serializers
from ..models.user_models import UserModel

class UserLoginSerializer(serializers.Serializer):

    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)


    def validate(self, attrs):
        
        return attrs