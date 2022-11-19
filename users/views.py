from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect

from users.forms import UserCreateForm, UserLoginForm


def home_view(request):
    return render(request, 'homepage.html')


def register_view(request):
    form = UserCreateForm()
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'register.html', context={'form': form})


def login_view(request):
    form = UserLoginForm()
    if request.method == 'POST':
        form = UserLoginForm(request, request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.data['username'], password=form.data['password'])
            if user.is_authenticated:
                login(request, user)
                return redirect('home')
    return render(request, 'login.html', context={'form': form})


def logout_view(request):
    logout(request)
    return render(request, 'homepage.html')
