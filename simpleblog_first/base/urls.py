from django.urls import path
from . import views



urlpatterns = [
    path('', views.Home, name='Home'),
    path('Home/', views.Home, name='Home'), 
     # Handles /Room without pk
    path('room/<str:pk>/', views.Room, name='Room'),
]


