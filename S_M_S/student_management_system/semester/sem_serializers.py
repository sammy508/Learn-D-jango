

from rest_framework import serializers
from yaml import serialize
from  ..models.semester_models import SemesterModel


class SemesterSerializers(serializers.ModelSerializer):

    class Meta:
        model = SemesterModel
        fields = "__all__"

