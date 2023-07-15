from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import *

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ('photo', 'gender', 'first_name', 'last_name', 'email')

class MyUserChangeForm(UserChangeForm):
    class Meta:
        model = MyUser
        fields = ('photo', 'gender', 'first_name', 'last_name', 'email')