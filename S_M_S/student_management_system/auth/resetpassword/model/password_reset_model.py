
from pyexpat import model
from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import timedelta
from django.utils import timezone


User =  get_user_model()

class PasswordReset(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=255, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    expires_at =  models.DateTimeField(default=lambda: timezone.now() + timedelta(minutes=30))


    def is_expired(self):
        return timezone.now() > self.expires_at

