

import uuid
from django.db import models
from django.forms import CharField
from ..utils import id_generators
from django.db import transaction
from ..utils.validations import NAME_VALIDATOR, PHONE_VALIDATOR


class TeachersModel(models.Model):
        t_id = models.AutoField(primary_key=True) # internal
       
        f_name = models.CharField(max_length=20, null=False, blank=False,validators=[NAME_VALIDATOR])  
        l_name = models.CharField(max_length=20, null=False, blank=False, validators=[NAME_VALIDATOR])  
        emp_id = models.CharField(max_length=10, unique=True, editable=False)
        phone = models.CharField(
            max_length=15,
            validators=[PHONE_VALIDATOR],  # your regex validator
            blank=True, null=True
        )



        def save(self, *args, **kwargs):
                
                if not self.emp_id:
                        with transaction.atomic():
                         last_teacher = TeachersModel.objects.order_by('-t_id').first()
                         last_id = int(last_teacher.emp_id.split('-')[1]) if last_teacher else 0


                        self.emp_id= id_generators.generate_id("EMP",last_id=last_id)
                        
                super().save(*args, **kwargs)




        class Meta:
                db_table = 'TeachersTable'