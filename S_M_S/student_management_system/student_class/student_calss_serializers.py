
from ..models.student_class_models import StudentClassModel
from rest_framework import serializers


class StudentClassSerializers(serializers.ModelSerializer):

     class Meta:
        model = StudentClassModel
        fields = "__all__" 