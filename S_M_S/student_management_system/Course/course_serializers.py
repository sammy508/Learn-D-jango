
from rest_framework import serializers
from ..Course.course_model import CourseModel

class CourseSerializer(serializers.ModelSerializer):


    class Meta:
        model = CourseModel

        fields = "__all__"
      