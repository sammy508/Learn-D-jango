
from os import name
from django.db import router
from django.urls import path, include

from .views.user_view import UserApiview
from .views.admin_only_view import UserCreateApiView
from .views.userlogin_view import UserloginApiView
from rest_framework.routers import DefaultRouter
from .views.userlogout_views import UserLogoutViews
from rest_framework_simplejwt.views import ( TokenObtainPairView, TokenRefreshView,  TokenVerifyView)
from .Course.course_views import CourseApiView, CourseSingalApiView
from  .auth.resetpassword.reset_password_view import  SendResetPasswordLinkView, ResetPaswordView, ChangepasswordView
from .Teacher.teacher_profile_view import TeacherView
from .Student.student_profile_view import StudentApiView
from .subjects.sub_views import SubjectAPIView,SingleSubjectApiView

# Subjects
from .semester.sem_views import SemesterApiView




urlpatterns = [

    path('users/', UserApiview.as_view(), name='user'),
    path('users/<uuid:pk>/', UserApiview.as_view()),
    path('create-user/',UserCreateApiView.as_view()),
    path('auth/custom-login/', UserloginApiView.as_view(), name='custom-login'),
    path('auth/logout-user/',UserLogoutViews().as_view()),
    path('api/auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # student 
    path('student/profile/',StudentApiView().as_view(),name="student-profile-list"),   # 
    path('student/profile/<int:pk>',StudentApiView().as_view(),name="student-profile"), # crud in del it only delete user profile image 
    
    #Courses
    path('courses/',CourseApiView.as_view(), name="Courses"),
    path('courses/<str:pk>',CourseSingalApiView().as_view(), name="Course"),

    # Auth
    path('send_resetlink/', SendResetPasswordLinkView.as_view(), name='forgetpassword'),
    path('auth/reset_password/<str:token>/', ResetPaswordView.as_view(), name= "reset_Password"),
    path('auth/change_password/', ChangepasswordView.as_view(), name='change_password'),
    
    # Teacer 
    path('teachers/',TeacherView.as_view(), name='teacher'),
    path('teacher/<int:pk>/',TeacherView.as_view(), name='teacher'),


    # Subjects
    path('subjects/',SubjectAPIView.as_view(), name='subjects'),
    path('subject/<str:pk>/',SingleSubjectApiView.as_view(), name='subject'),

    # Semester 
    path('semesters/',SemesterApiView.as_view(), name = 'Semesters')
]

