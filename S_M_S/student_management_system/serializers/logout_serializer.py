

from rest_framework import serializers
from ..models.user_models import UserModel

class UserLogoutSerializer(serializers.Serializer):

    refresh = serializers.CharField(
             write_only=True,
        required=True,
        help_text="Refresh token to be blacklisted on logout"
    )

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

  

    
  