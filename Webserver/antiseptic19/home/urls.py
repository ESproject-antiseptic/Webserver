from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('test',views.test, name="test"),
    path('make_room', views.make_room, name="make_room"),  # 방만들기
    path('enter_room', views.enter_room, name="enter_room"),  # 방들어가기
    path('uimage/', views.test, name='uimage'),
    path('test/', views.test, name='dface'),
    path('test1/', views.test1, name='test1'),
    path('cam/', views.cam, name='cam'),
    path('index/', views.index, name='index'),

]