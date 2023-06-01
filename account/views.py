from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.views.generic import CreateView
from django.http import HttpResponse
from .forms import LoginForm


class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = '/'


def profile(request):
    return render(request, 'profile.html')


def index(request):
    return HttpResponse('Hello world!!')


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})
