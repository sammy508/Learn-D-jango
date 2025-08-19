from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.core.validators import RegexValidator

# Create your models here.




class Topic(models.Model):
    name = models.CharField(max_length=200)
    

    def __str__(self):
        return self.name

class Room(models.Model):
    host= models.ForeignKey(User, on_delete=models.SET_NULL, null= True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null= True)
    name = models.CharField(max_length=50, null=False)
    description = models.TextField(null= True, blank= True, max_length= 1000)

    # participants
    updated = models.DateTimeField(auto_now= True)
    created = models. DateTimeField(auto_now_add=True)

    
    class Meta:
        ordering = ['-updated', '-created']


    def __str__(self ):
        return self.name
  

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]

class registerUser(AbstractUser):
    email_validator = RegexValidator(
    regex=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}$',
    message="Enter a valid email address"
)
    phone = models.CharField(max_length=10,blank=False, null=False)
    email= models.EmailField(unique=True,validators=[email_validator],max_length=50, null=False, blank=False )






