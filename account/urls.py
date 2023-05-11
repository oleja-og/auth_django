from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .views import RegisterUser, index

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('', index)
]
