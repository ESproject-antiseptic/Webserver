# Generated by Django 3.0.8 on 2020-10-08 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=64, unique=True, verbose_name='이메일')),
                ('password', models.CharField(max_length=64, verbose_name='비밀번호')),
                ('name', models.CharField(max_length=64, verbose_name='이름')),
                ('userimage', models.ImageField(upload_to='', verbose_name='사용자이미지')),
            ],
        ),
    ]
