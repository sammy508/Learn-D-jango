
from tkinter import CASCADE
from typing import cast
from django.db import models
from django.db import transaction
from django.contrib.auth.models import User
from django.conf import settings
from django.core.validators import MinLengthValidator


class StudentEnrollmentModel(models.Model):
    enroll_id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey('StudentModel',on_delete=models.CASCADE, related_name='enrollments' )
    class_id = models.ForeignKey('SubjectsModel', on_delete= models.CASCADE, related_name='class')
    enroll_at = models.DateField( auto_now_add=True)

    STATUS_CHOICES = [
        ("active", "Active"),
        ("dropped", "Dropped"),

    ]
    default_status = STATUS_CHOICES[0][0]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES,default= default_status)

    promoted_at = models.DateField(auto_now=True, blank=False)
    grade = models.CharField(validators=[MinLengthValidator(1)],max_length=1, blank=False)
    cgpa = models.DecimalField(max_digits=4, decimal_places=2)
    current_sem = models.ForeignKey(
        'SemesterModel',
        on_delete=models.CASCADE,
        related_name='enrolled_students'
        )
    

    def __str__(self):
        return f"{self.student_id} - {self.current_sem.sem_name} ({self.status})"
