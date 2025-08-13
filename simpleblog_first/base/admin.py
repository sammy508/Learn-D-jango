from django.contrib import admin
from .models import Room, Topic, Message
# Register your models here.

# admin.site.register(Room, Topic, Message)   # It doesn't accepts multiple value like this we have to create pass seperately 

admin.site.register(Room)
admin.site.register(Message)
admin.site.register(Topic)