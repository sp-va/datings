from django.shortcuts import render, redirect
from media.myapi.watermark import watermark
from .forms import MyUserCreationForm

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
            username = form.cleaned_data['username']
            photo = form.cleaned_data['photo']
            photo.name = f'{username}.jpg'
            user = form.save(commit=False)
            user.photo = photo
            user.save()
            watermark(f'media/myapi/{username}.jpg')

            return redirect('main')

        context = {'form': form}
        return render(request, 'myapi/create.html', context)
    context = {'form': MyUserCreationForm()}
    return render(request, 'myapi/create.html', context)

