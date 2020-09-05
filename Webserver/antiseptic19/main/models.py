from django.db import models

# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=64,verbose_name = '이메일')
    password = models.CharField(max_length=64,verbose_name = '비밀번호')
    name = models.CharField(max_length=64,verbose_name = '이름')
    userimage = models.ImageField(verbose_name = '사용자이미지')

    def __str__(self):
        return self.email
