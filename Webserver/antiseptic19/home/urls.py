from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('make_room', views.make_room, name="make_room"),  # 방만들기
    path('enter_room', views.enter_room, name="enter_room"), # 방들어가기
    path('myroom', views.myroom, name="myroom"),
    path('myroom1', views.myroom1, name="myroom1"),  #내가만든방 목록

    path('app_roomnumber',views.app_roomnumber),
    path('app_makeroom',views.app_makeroom),
    path('app_makemyroom',views.app_makemyroom),

]