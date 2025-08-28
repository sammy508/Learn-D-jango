
from django.urls import path

# import your views here
from .views.post_views import * # importing all the view function of that page

urlpatterns = [
    path('posts/', post_list, name='post-list'),
]
