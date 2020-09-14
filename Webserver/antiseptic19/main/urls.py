from django.urls import path
from . import views
#Router 부분


urlpatterns = [
    path('', views.login, name='main'),
    path('home/',views.home, name = "home"),
    path('signup', views.signup, name='signup'),
    path('logout',views.logout,name='logout'),
    path('home/mypage',views.mypage, name="mypage"),
    path('dropout',views.dropout, name="dropout"),
    path('edit',views.edit, name="edit"),



    #APP
    path('app_signup', views.app_signup, name='app_signup'),
    path('app_login',views.app_login),
    path('app_image',views.app_image),
    path('app_delete',views.app_delete),
    path('app_modify',views.app_modify)
]