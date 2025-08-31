
from rest_framework import serializers
from ..models.course_model import CourseModel

class CourseSerializer(serializers.ModelSerializer):


    class Meta:
        model = CourseModel
        fields = "__all__"    # Applied automatic serializers instead of handling manually
