
from django.urls import path

from api import views

# importing all the view function of that page
from .views.student_views import Studentview, StudentDetailView


urlpatterns = [
    path('student/',Studentview, name='student'),
    path('student/<str:pk>',StudentDetailView, name='student_detail'),
]
