
from rest_framework import serializers
from ..models.studentmodel import student

class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = '__all__'
