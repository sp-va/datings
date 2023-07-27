from django.urls import path
from .views import *

urlpatterns = [

    path('clients/<int:id>/match', user_info,  name='match'),
    path('', main, name='main'),
    path('clients/create', create, name='create'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', logout_func, name='logout'),
    path('users_list/', users_list, name='users_list'),

]

