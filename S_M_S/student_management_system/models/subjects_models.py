
# from django.db import models
# from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
# from django.core.validators import EmailValidator
# import uuid
# from django.core.validators import MinLengthValidator




# class ClassModel(models.Model):
#     cs_id = models.AutoField(primary_key=True)
#     cs_name = models.CharField(max_length= 50,validators=[MinLengthValidator(3)])
    
   

from tkinter import CASCADE
from django.db import models
from django.db import transaction
from django.contrib.auth.models import User
from django.conf import settings
from django.core.validators import MinLengthValidator
# from ..semester.sem_models import SemesterModel



class SubjectsModel(models.Model):
    sub_id = models.CharField(primary_key=True)
    sem_id = models.ForeignKey('SemesterModel',on_delete=models.CASCADE)
    sub_name = models.CharField(max_length=50,validators=[MinLengthValidator(3)],blank=False, null=False )
    sub_code = models.CharField(max_length=6, validators=[MinLengthValidator(6)], blank=False, null=False, unique=True)
    sub_credit = models.PositiveSmallIntegerField()
    sub_descriptions = models.TextField(blank=True, null=True, max_length=200)
    TYPE_CHOICES = [
    ('core', 'Core'),
    ('elective', 'Elective'),
    ('lab', 'Lab'),
    ('project', 'Project')
    ]
    subject_type = models.CharField(max_length=10, choices=TYPE_CHOICES, default='core')

    class Meta:
        db_table = 'SubjectsModel'
        app_label = "student_management_system"



