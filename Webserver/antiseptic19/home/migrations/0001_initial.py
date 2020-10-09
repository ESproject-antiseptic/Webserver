# Generated by Django 3.0.8 on 2020-10-08 05:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_name', models.CharField(max_length=64, verbose_name='방이름')),
                ('room_ps', models.CharField(max_length=64, verbose_name='방비밀번호')),
                ('room_member', models.FileField(default=None, upload_to='', verbose_name='회원명단')),
                ('room_func', models.CharField(max_length=64, verbose_name='방기능')),
                ('room_member_list', models.CharField(default=None, max_length=64, verbose_name='회원명단리스트')),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.User', verbose_name='방관리자')),
            ],
        ),
    ]
