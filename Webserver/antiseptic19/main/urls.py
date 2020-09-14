from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='main'),
    path('signup', views.signup, name='signup'),
    path('logout',views.logout,name='logout'),
    path('home/mypage',views.mypage, name="mypage"),
    path('dropout',views.dropout, name="dropout"),#회원삭제

    #APP
    path('app_signup', views.app_signup, name='app_signup'),
    path('app_login',views.app_login),
    path('app_image',views.app_image),
    path('app_delete',views.app_delete),
    path('app_modify',views.app_modify)
]