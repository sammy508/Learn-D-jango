from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


# urlpatterns = [
#     path('', views.Home, name='Home'),
#     path('Home/', views.Home, name='Home'), 
#      # Handles /Room without pk
#     path('room/<str:pk>/', views.Rooms, name='room'),
# ]


urlpatterns = [
    path('registration/', views.userRegistration_Form, name = 'registration'),
    path('LoginPage/', views.LoginPage, name='LoginPage'),
    path('logout', views.Logoutbutton, name = 'logout'),
   

    path('', views.Home, name='Home'),
    path('Home/', views.Home, name='Home'), 
    path('room/<str:pk>/', views.Rooms, name='room'),
    path('Create_Room', views.Create_Room, name='Create_Room'),
    path('update_Room/<str:pk>/',views.update_Room, name='update_Room'),
    path('delete_Room/<str:pk>/', views.delete_Room, name='delete_Room'),
    
]


# To upload and provide path to the profile images 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)