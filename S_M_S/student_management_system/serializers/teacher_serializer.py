
from rest_framework import serializers
from ..models.Teacher_table import TeacherModel

class TeacherSerializer(serializers.ModelSerializer):


    class Meta:
        model= TeacherModel
        fields = "__all__"    # Applied automatic serializers instead of handling manually
