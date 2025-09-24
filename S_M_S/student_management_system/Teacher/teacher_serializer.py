
from rest_framework import serializers
# from .teacher_models import TeacherModel
from .teacher_model import TeachersModel

class TeacherSerializer(serializers.ModelSerializer):


    class Meta:
        model= TeachersModel
        fields = "__all__"    # Applied automatic serializers instead of handling manually
