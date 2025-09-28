
from rest_framework import serializers
from ..models.student_enrollment_models import StudentEnrollmentModel


class StudentEnrollmentSerializer(serializers.ModelSerializer):

     class Meta:
        model = StudentEnrollmentModel
        fields = "__all__"
      