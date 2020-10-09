from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *   #같은 경로의 models.py에서 User라는 클래스를 임포트한다.

# Register your models here.

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('admin', 'room_name','room_ps','room_member','room_func')  #,'userimage'
    list_filter = ('admin',)


