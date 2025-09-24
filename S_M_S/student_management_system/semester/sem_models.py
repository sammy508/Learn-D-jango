
# from pyexpat import model
# from tkinter import CASCADE
# from typing import Required
# from django.db import models
# import uuid
# from django.core.validators import MinValueValidator, MaxValueValidator


# class SemesterModel(models.Model):
#     sem_id = models.CharField(primary_key=True)
#     sem_name = models.CharField(max_length=25, blank=False, null=False)
#     course_id = models.ForeignKey('CourseModel', on_delete= models.CASCADE)
#     sem_num = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(8)])
#     start_date = models.DateField()     
#     end_date = models.DateField()
                                                                                                                                                                            
#     class Meta: 
#         db_table = 'SemesterModel'
#         app_label = "student_management_system"
    