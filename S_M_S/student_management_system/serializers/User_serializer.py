
from pyexpat import model
from rest_framework import serializers
from ..models.user_models import UserModel

class Userserializer(serializers.ModelSerializer):


    class Meta:
        model= UserModel
        fields = "__all__"    # Applied automatic serializers instead of handling manually


    
