from django.contrib import admin
from .models import *   #같은 경로의 models.py에서 User라는 클래스를 임포트한다.

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'name','password')  #,'userimage'

