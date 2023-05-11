from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.views.generic import CreateView
from django.http import HttpResponse


class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = '/'


def profile(request):
    return render(request, 'profile.html')

def index(request):
    return HttpResponse('Hello world!!')
