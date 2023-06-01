from django.urls import path, re_path

from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .views import RegisterUser, index

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.user_login, name='login'),
]
