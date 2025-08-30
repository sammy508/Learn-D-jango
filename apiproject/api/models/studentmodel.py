
# from django.db import models

# class Post(models.Model):
#     title = models.CharField(max_length=100)
#     body = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.title

import uuid
from django.db import models
from django.core.validators import RegexValidator



class student(models.Model):
    # id = models.UUIDField(unique=True,primary_key=True, auto_created=True)

    id = models.UUIDField(
        primary_key=True, 
        default=uuid.uuid4,  # auto-generate a unique UUID
        editable=False
    )


    username = models.CharField(max_length=20,verbose_name='username', blank=True,
                                 validators=[RegexValidator(r'^[a-zA-Z ]+$', 'Only letters and spaces are allowed.')])
    
    email = models.EmailField(unique=True,
                               blank=False,
                               default='example@gmail.com')
    
    phone = models.CharField(
        max_length=15,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
            )
        ]
    )


def __str__(self):
        return self.username or str(self.id)


class Meta:
      db_table = "student"