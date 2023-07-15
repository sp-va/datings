from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect


from .forms import MyUserCreationForm
from .models import *

menu = [
    {'title' : 'Главная страница', 'url_name' : 'main'},
]

def main(request):
    return render(request,
                  'myapi/main.html',
                  {'title' : 'Главная страница', 'menu' : menu})



def create(request):
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            user.save()
            return redirect('main')
        context = {'form': form}
        return render(request, 'myapi/create.html', context)
    context = {'form': MyUserCreationForm()}
    return render(request, 'myapi/create.html', context)