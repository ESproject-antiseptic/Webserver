from django.db import models
from main.models import *
# Create your models here.
class Room(models.Model):
    admin = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name = '방관리자')
    room_name = models.CharField(max_length=64, verbose_name='방이름')
    room_ps = models.CharField(max_length=64,verbose_name = '방비밀번호')
    room_member = models.FileField(verbose_name = '회원명단',default=None) #엑셀파일로 받기
    room_func = models.CharField(max_length=64, verbose_name='방기능')

    def __str__(self):
        return self.room_name

class ImageUploadModel(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.ImageField(upload_to = 'images/%Y/%m/%d')
    uploaded_at = models.DateTimeField(auto_now_add=True)