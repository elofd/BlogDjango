from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.views import LogoutView, LoginView
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .models import CustomUser
from .forms import CustomUserCreationForm


class SignUpView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('blog:post_list')


class MyLogoutView(LogoutView):
    next_page = reverse_lazy("blog:post_list")


class MyLoginView(LoginView):
    template_name = 'users/login.html'
    next_page = reverse_lazy('blog:post_list')

