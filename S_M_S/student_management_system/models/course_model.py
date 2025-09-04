
from pickle import TRUE
import uuid
from django.db import models
from ..utils.validations import ValidateFields
from ..utils import id_generators



class CourseModel(models.Model):
        course_id = models.AutoField(primary_key=True) # internal
       
        course_name = models.CharField(max_length=20,null=False, blank=False, validators=[ValidateFields.namefield_validator()])
        course_code = models.CharField(max_length=5, unique=True)
        total_sem = models.IntegerField(default=8)
        course_image = models.ImageField(upload_to='Courses/',null=True,blank=True )
        

        def delete_image(self):
                if self.avatar:
                        self.avatar.delete(save=False,) # removes file from storage
                        self.avatar = None
                        self.save()



        class Meta:
                db_table = 'CourseTable'