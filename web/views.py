from django.contrib import messages
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout

from .forms import UserRegistrationForm


def home(request):
    return render(request, 'base.html')

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
