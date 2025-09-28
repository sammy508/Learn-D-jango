

from django.db import models
from django.db import transaction
from django.contrib.auth.models import User
from django.conf import settings
from django.core.validators import MinLengthValidator



class ClassModel(models.Model):
    cs_id = models.IntegerField(primary_key=True)
    cs_name = models.CharField(validators=[MinLengthValidator(3)],max_length=50)
    section = models.CharField(max_length=2)
    year = models.PositiveBigIntegerField(null=True, blank=True)
    batch = models.CharField(max_length=20, null=True, blank=True)

    #Links
    semester = models.ForeignKey('SemesterModel',on_delete=models.CASCADE)
    course = models.ForeignKey('CourseModel',on_delete=models.CASCADE)

    # Meta info
    is_activated = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self) :
        return  f"{self.course.course_name} - Sem {self.semester.sem_num} - Section {self.section}"
