from django.urls import path
from . import views
#Router 부분 
from rest_framework import routers
from rest_framework.response import Response
from rest_framework.views import APIView








urlpatterns = [
    path('', views.login, name='main'),
    path('signup', views.signup, name='signup'),
    path('app_signup', views.app_signup, name='app_signup'),
    path('app_login',views.app_login)
    # path('main/',views.main, name="main")
]