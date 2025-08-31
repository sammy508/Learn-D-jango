
from django.db import models
from django.forms import CharField
from ..utils.validations import ValidateFields
from django.contrib.auth.hashers import make_password, check_password  # to hash password and check hashed and unhashed password 
from ..utils.hasher import hash_password, check_password, verify_password




class UserModel(models.Model):
    
    id = models.AutoField(primary_key=True) # internal

    username = models.CharField(
        blank=False,
        null=False,
          validators= [ ValidateFields.Username_validator()]
    )
   
    email = models.EmailField(unique=True,
                              null=False,
                               blank=False,
                               validators=[ValidateFields.Email_validator()],
                               
                               default='example@gmail.com')
    
    usr_password = models.CharField(max_length=130, validators=[ValidateFields.password_validator()]                              
                                     )
    
  

    # Helps to assign roles to the User 
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    ]

    roles = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default= ROLE_CHOICES[2][0]   # Used list property to access and assign default user # 'student' value
    )


    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    # Model level password hashing 

    def save(self, *args, **kwargs):
          
          if not self.pk or not self.usr_password.startswith('pbkdf2_'):
            self.usr_password = hash_password(self.usr_password)
            super().save(*args, **kwargs)


     # check_password is  helper function  for login validation 

    def check_password(self, raw_password):
         return verify_password(raw_password, self.usr_password)
   

    class Meta:
                db_table = 'UserTable'