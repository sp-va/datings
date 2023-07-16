from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import *
from django import forms
class MyUserCreationForm(UserCreationForm):
    photo = forms.ImageField(required=True)
    class Meta:
        model = MyUser
        fields = ('photo', 'gender', 'first_name', 'last_name', 'email', 'username')

class MyUserChangeForm(UserChangeForm):
    class Meta:
        model = MyUser
        fields = ('photo', 'gender', 'first_name', 'last_name', 'email', 'username')