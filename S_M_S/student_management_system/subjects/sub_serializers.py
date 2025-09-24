
from rest_framework import serializers
from ..models.subjects_models import SubjectsModel

class SubjectSerializers(serializers.ModelSerializer):

    class Meta:
        model = SubjectsModel
        fields = "__all__"