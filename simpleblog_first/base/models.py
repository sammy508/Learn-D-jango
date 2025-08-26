from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django import forms
from django.contrib.auth.forms import UserCreationForm
import os
from django.db.models.signals import post_save
from django.dispatch import receiver

# from django.core.validators import RegexValidator

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

    participants = models.ManyToManyField(User, related_name= 'participants', blank=True)  # herehow we write many to many relations on django orm
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


class Userprofile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # username = models.CharField(User, max_length=20, blank=False, null=False, verbose_name ="Username")    # if i pass User, then i dont have to pass verbose_name, it automatically takes verbosename
    username = models.CharField(max_length=20, blank=False, null=False, verbose_name="Username")

    email = models.EmailField(unique=True,max_length=20,null=False,blank=False, verbose_name='Email address' )
    phone = models.CharField(max_length=10, null=False, blank= False,verbose_name='Phone num')
    profile_image = models.ImageField(blank=False, null=False, upload_to='profile_images/',default='default_profile.png')
    bio = models.TextField(blank=True, null=True, max_length=50)

    created_at = models.DateTimeField(auto_now_add= True )
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return super().__str__()
    
    def delete(self, *args, **kwargs):
        if self.profile_image and self.profile_image.name != 'default_profile.png':
            if os.path.isfile(self.profile_image.path):
                os.remove(self.profile_image.path)
                super().delete(*args, **kwargs)




# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Userprofile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.userprofile.save()





















# It's easier to use nad handle default registraition form so switch to user model and built in form 
# class _registerUser(models.Model):
#     email = forms.EmailField(required=True)

#     class Meta:
#         model = User
#         fields = ('user', 'email', 'password','confirm password')
    



