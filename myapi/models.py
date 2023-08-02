from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator



class MyUser(AbstractUser):
    GENDERS = [
        ('М', 'Мужчина'),
        ('Ж', 'Женщина'),
    ]

    gender = models.CharField(max_length=7, choices=GENDERS)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    photo = models.ImageField(upload_to='myapi/', blank=True, null=True)
    #username = models.CharField(unique=True,
                                #max_length=50,
                                #validators=[RegexValidator(r'^[a-zA-Z0-9]+$',
                                                           #'Only alphanumeric characters are allowed.')],
                                #)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class UsersMatching(models.Model):
    sender_email = models.EmailField()
    receiver_email = models.EmailField()

    def __str__(self):
        return f'Пользователю {self.user1_email} нравистя пользователь {self.user2_email}'