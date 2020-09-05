from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('make_room', views.make_room, name="make_room"),  # 방만들기
    path('enter_room', views.enter_room, name="enter_room"),  # 방들어가기

]