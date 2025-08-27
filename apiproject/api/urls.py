
from django.urls import path

# import your views here
from .views import post_list  # adjust if your view is named differently

urlpatterns = [
    path('posts/', post_list, name='post-list'),
]
