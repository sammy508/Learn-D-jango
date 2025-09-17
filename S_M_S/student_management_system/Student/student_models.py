
from ast import Delete
import uuid
from django.db import models
from django.forms import CharField
from django.core.validators import MinLengthValidator
from ..utils.validations import NAME_VALIDATOR, PHONE_VALIDATOR
from django.db import transaction
from ..utils import student_id_generator
from django.contrib.auth.models import User
from django.conf import settings




from django.db import transaction 

class StudentModel(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    st_id = models.AutoField(primary_key=True)  # internal
    f_name = models.CharField(
        max_length=20,
        null=False,
        blank=False,
        validators=[NAME_VALIDATOR]
        
    )
    l_name = models.CharField(
        max_length=20,
        null=False,
        blank=False,
        validators=[NAME_VALIDATOR]
    )

    phone = models.CharField(
            max_length=15,
            validators=[PHONE_VALIDATOR],  # your regex validator
            blank=True, null=True
        )
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)


    course = models.ForeignKey('CourseModel', on_delete= models.PROTECT)  # Links to course and prevents from delete

    enroll_id = models.CharField(max_length=15, unique=True, editable=False)

    current_sem = models.IntegerField(default=1)  # optional

    def save(self, *args, **kwargs):
        if not self.enroll_id:  # generate only if new record
            with transaction.atomic():
                # Get last student ID
                last_student = StudentModel.objects.filter(course=self.course).order_by('-st_id').first()
                last_number = int(last_student.enroll_id.split('-')[1]) if last_student else 1000

                # Generate new enroll_id
                self.enroll_id = f"Stu-{self.course.course_code}-{last_number + 1}"

        super().save(*args, **kwargs)


    def delete_avatar(self):
        if self.avatar:
            self.avatar.delete(save=False,) # removes file from storage
            self.avatar = None
            self.save()
           





    class Meta:
        db_table = 'StudentTable'



        # May have to update student id later and make unique to generate add collegename-createddatestamp-number in this format which makes id uniques each time anc can repeat number in endpart 