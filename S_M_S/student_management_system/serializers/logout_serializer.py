

from rest_framework import serializers
from ..models.user_models import UserModel

from rest_framework import serializers

class UserLogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField(
        write_only=True,
        required=True,
        help_text="Refresh token to be blacklisted on logout"
    )