from contextlib import redirect_stderr
from django.contrib import messages
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout


from .forms import (
    UserRegistrationForm, UserLoginForm
)

def home(request):
    return render(request, 'base.html')


'''
    Autentification, registration and logout function 
'''
def sign_in(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    context = {
        'form': form,
        'title': 'Registration'
        }
    return render(
        request, 
        'login.html', 
        context=context)

def user_logout(request):
    logout(request)
    return redirect('login')

def registrate(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'auth are successful')
            return redirect('home')
        else:
            messages.error(request, 'Invalid data')
    else:
        form = UserRegistrationForm()
    context = {
        'form': form,
        'title': 'Registration'
        }
    return render(
        request, 
        'registrate.html', 
        context=context)
