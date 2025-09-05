

from email.mime import image
from rest_framework import serializers

from ..models.user_models import UserModel

from ..models.student_models import StudentModel
from ..models.course_model import CourseModel
from PIL import Image

class StudentProfileSerializer(serializers.ModelSerializer):
    course = serializers.PrimaryKeyRelatedField(queryset=CourseModel.objects.all())
    user = serializers.PrimaryKeyRelatedField(queryset=UserModel.objects.all())

    class Meta:
        model = StudentModel
        fields = "__all__"    # Applied automatic serializers instead of handling manually

    def validate_avatar(self, value):
        max_size= 2*1024*1024

        if value.size> max_size:
            raise serializers.ValidationError("Image size should not exceed 2MB..")
        
        img = Image.open(value)

        if img.width > 2000 or img.height > 2000:
            raise serializers.ValidationError("Image dimensions should not exceed 2000x2000px.")
        return value
#  Have to add paginations later in both student, course and users views