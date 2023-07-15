from django.db import models
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
    GENDERS = [
        ('М', 'Мужчина'),
        ('Ж', 'Женщина'),
    ]

    gender = models.CharField(max_length=7, choices=GENDERS)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    photo = models.ImageField(upload_to='media/photo', blank=True, null=True)
    def __str__(self):
        self.username = self.username + ' ' + self.first_name + ' ' + self.last_name
        return self.username
