from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import MyUser
from .forms import MyUserCreationForm, MyUserChangeForm

class MyUserAdmin(UserAdmin):
    add_form = MyUserCreationForm
    form = MyUserChangeForm
    model = MyUser
    list_display = ['photo', 'gender', 'first_name', 'last_name', 'email']

admin.site.register(MyUser)