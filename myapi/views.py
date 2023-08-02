from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from media.myapi.watermark import watermark
from .forms import *
from .models import *
from django.contrib.auth import logout
from django.contrib import messages
from .utils import matching_users



menu_if_logged_in = [
    {'title': 'Выход из аккаунта', 'url_name': 'logout'},
    {'title': 'Список пользователей', 'url_name': 'users_list'},
    #{'title': 'Личный кабинет для редактирования своих данных', 'url_name': 'my_account'},

]
menu_if_NOT_logged_in = [
    {'title': 'Создать аккаунт', 'url_name': 'create'},
    {'title': 'Вход в аккаунт', 'url_name': 'login'},

]


# Главная страница
def main(request):
    current_user = request.user
    authenticated = request.user.is_authenticated
    context = {"authenticated": authenticated,
               "menu_if_NOT_logged_in": menu_if_NOT_logged_in,
               "menu_if_logged_in": menu_if_logged_in,
               'current_user': current_user
               }
    return render(request,
                  'myapi/main.html', context=context)


# Создание пользователя
def create(request):
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data['username']
            photo = form.cleaned_data['photo']
            photo.name = f'{username}' + '_' + photo.name
            user = form.save(commit=False)
            user.photo.name = photo.name
            user.save()
            watermark(f'media/myapi/{photo.name}')

            return redirect('main')

        context = {'form': form}
        return render(request, 'myapi/create.html', context=context)
    context = {'form': MyUserCreationForm()}
    return render(request, 'myapi/create.html', context)


# Старая попытка
'''
def login(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('main')
        form = LoginForm()
        return render(request, 'myapi/login.html', {'form': form})
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            login(user)
            return redirect('main')

            form = LoginForm()
        return render(request, 'myapi/login.html', {'form': form})
        
'''


# Вот это для входа в акк
class UserLoginView(LoginView):

    def get_success_url(self):
        return reverse_lazy('main')

    def form_invalid(self, form):
        messages.error(self.request, 'Неверная почта либо пароль')
        return self.render_to_response(self.get_context_data(form=form))


def logout_func(request):
    logout(request)
    return redirect('main')


# Информация о пользователе и ОЦЕНКА
@login_required(redirect_field_name='login')
def user_info(request, id):

    user = get_object_or_404(MyUser, pk=id)
    current_user = request.user
    user1_email = user.email
    user2_email = current_user.email

    context = {
        'user': user,
        'current_user': current_user,
    }

    if request.method == 'POST':
        UsersMatching.objects.get_or_create(sender_email=user2_email, receiver_email=user1_email)
        return HttpResponse('лайк добавлен')


        #matching_users(user1_email, user2_email)
        #if user_1_to_2 and user_2_to_1:
        #return render(request, 'myapi/main.html', context=context)


    return render(request, 'myapi/match.html', context=context)


#Список пользователей для оценки
@login_required(redirect_field_name='login')
def users_list(request):
    current_user = request.user
    excluded_pk = [1, current_user.id]
    users_list = MyUser.objects.exclude(Q(pk__in=excluded_pk))
    context = {
        "users_list": users_list,
    }
    return render(request, 'myapi/users_list.html', context=context)

