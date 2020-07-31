from django.urls import path
from . import views
#Router 부분


urlpatterns = [
    path('', views.login, name='main'),
    path('home/',views.home, name = "home"),
    path('signup', views.signup, name='signup'),
    path('app_signup', views.app_signup, name='app_signup'),
    path('app_login',views.app_login)
]