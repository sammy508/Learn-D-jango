

from django.db import models
from django.db import transaction
from django.contrib.auth.models import User
from django.conf import settings
from django.core.validators import MinLengthValidator
import uuid

class StudentClassModel(models.Model):
   
   sc_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

   class_obj = models.ForeignKey('Classmodel',on_delete=models.CASCADE)
   student = models.ForeignKey('StudentModel', on_delete=models.CASCADE)

   status = models.CharField(
        max_length=20,
        choices=[("active", "Active"), ("backlog", "Backlog"), ("repeated", "Repeated")],
        default="active" )
   
   date_joined = models.DateField(auto_now_add=True)
   date_left = models.DateField(null=True, blank=True)

      

   class Meta:
        constraints = [
            models.UniqueConstraint(fields=['student', 'class_obj'], name='unique_student_class_sem')

        ]   #"""It tells Django (and the underlying database):
#       👉 “For this table, the combination of student and class_obj must be unique.”"""
   


