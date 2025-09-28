
from pyexpat import model
from rest_framework import serializers
from ..models.class_model import ClassModel

class ClassSerializers(serializers.ModelSerializer):

    class Meta:
        model = ClassModel
        fields = "__all__"