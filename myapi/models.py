from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class MyUser(AbstractUser):
    GENDERS = [
        ('М', 'Мужчина'),
        ('Ж', 'Женщина'),
    ]
    photo = models.ImageField(upload_to='media/photo', blank=True, null=True)
    gender = models.CharField(max_length=7, choices=GENDERS)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    def __str__(self):
        return self.username
