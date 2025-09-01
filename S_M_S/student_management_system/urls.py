
from django.db import router
from django.urls import path, include

from .views.user_view import UserApiview
from .views.admin_only_view import UserCreateApiView
from .views.userlogin_view import UserloginApiView
from rest_framework.routers import DefaultRouter
from .views.userlogout_views import UserLogoutViews
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)




urlpatterns = [

    path('users/', UserApiview.as_view(), name='user'),
    path('users/<int:pk>/', UserApiview.as_view()),
    path('create-user/',UserCreateApiView.as_view()),
    path('auth/custom-login/', UserloginApiView.as_view(), name='custom-login'),
    path('auth/logout-user/',UserLogoutViews().as_view()),
    path('api/auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # path('', include(router.urls)),

]

