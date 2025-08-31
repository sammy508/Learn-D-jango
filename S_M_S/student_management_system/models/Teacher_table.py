
import uuid
from django.db import models
from django.forms import CharField
from ..utils import id_generators
from django.db import transaction
from ..utils.validations import ValidateFields


class TeacherModel(models.Model):
        t_id = models.AutoField(primary_key=True) # internal
       
        f_name = models.CharField(max_length=20,null=False, blank=False, validators=[ValidateFields.namefield_validator()])
        l_name = models.CharField(max_length=20,null=False, blank=False, validators=[ValidateFields.namefield_validator()])

        emp_id =models.CharField(max_length=10, unique=True, editable=False)


        def save(self, *args, **kwargs):
                
                if not self.emp_id:
                        with transaction.atomic():
                         last_teacher = TeacherModel.objects.order_by('-id').first()
                         last_id = int(last_teacher.emp_id.split('-')[1]) if last_teacher else 0


                        self.emp_id= id_generators.generate_id("EMP",last_id=last_id)
                        
                super().save(*args, **kwargs)




        class Meta:
                db_table = 'TeacherTable'