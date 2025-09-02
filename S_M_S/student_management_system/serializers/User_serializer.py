
import email
from pyexpat import model
from wsgiref import validate
from ..models.user_models import UserModel


# serializers.py
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password


class Userserializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password]  # Django's built-in validation
    )
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = UserModel
        fields = ['email','id', 'password','password2', 'role']

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Passwords don't match"})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')  # Remove confirmation field
        password = validated_data.pop('password')
        
        user = UserModel(**validated_data)
        user.set_password(password)  # This hashes the password properly
        user.save()
        
        return user

    def update(self, instance, validated_data):
        # Handle password update if provided
        password = validated_data.pop('password', None)
        validated_data.pop('password2', None)
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        if password:
            instance.set_password(password)
        
        instance.save()
        return instance