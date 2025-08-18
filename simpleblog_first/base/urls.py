from django.urls import path
from . import views



# urlpatterns = [
#     path('', views.Home, name='Home'),
#     path('Home/', views.Home, name='Home'), 
#      # Handles /Room without pk
#     path('room/<str:pk>/', views.Rooms, name='room'),
# ]


urlpatterns = [
    path('', views.Home, name='Home'),
    path('Home/', views.Home, name='Home'), 
    path('room/<str:pk>/', views.Rooms, name='room'),
    path('Create_Room', views.Create_Room, name='Create_Room'),
    path('update_Room/<str:pk>/',views.update_Room, name='update_Room'),
    path('delete_Room/<str:pk>/', views.delete_Room, name='delete_Room'),
    
]
