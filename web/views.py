from copy import deepcopy
from django.http import Http404
from django.contrib import messages
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.views.generic import ListView, DetailView
from django.utils.datastructures import MultiValueDictKeyError


from .forms import (
    UserRegistrationForm, UserLoginForm, NewsForm
)
from .models import News 

ANON = 'AnonymousUser'


def home(request):
    context = {
        'title': 'Home'
    }
    return render(request, 'home.html', context=context)

def doesntexist(request, exception):
    return render(request, '404error.html', 
    context={
        'title': 'doesnt exist'
    }
    )

"""
block with creating/viewing/editing news
"""

def edit_form_data(form, query_news) -> dict:
    result = deepcopy(dict(form))
    result['title'] = query_news.title
    result['content'] = query_news.content
    result['publicated'] = query_news.publicated
    return result

def create_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            try:
                take = form.data['publicated']
                publicated = True
            except MultiValueDictKeyError:
                publicated = False
                
            author = User.objects.get(username=request.user.username)
                
            created_news = News(
                title=form.data['title'],
                content=form.data['content'],
                author=author,
                publicated=publicated,
            )

            created_news.save()
            return redirect('news')
    else:
        form = NewsForm()
    context = {
        'title': 'Creating...',
        'form': form,
    }
    return render(
        request, 'edit_news.html', context
    )

def editing_concrete_news(request, news_id):
    try:
        query = News.objects.get(pk=int(news_id))
    except:
        raise Http404('Doesnt exist(')
    
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            query.title = form.data['title']
            query.content = form.data['content']
            try:
                pub = form.data['publicated']
                query.publicated = True
            except MultiValueDictKeyError:
                query.publicated = False
            query.save()
            return redirect('news')
    else:
        form_data = edit_form_data(request.POST, query)
        form = NewsForm(data=form_data)
    context = {
        'title': 'Editing ...',
        'form': form,
    }
    return render(
        request, 'edit_news.html', context
    )

def concrete_news(request, news_id):
    try:
        query = News.objects.get(pk=int(news_id))
    except:
        raise Http404('Doesnt exist(')
    context = {
        'title': query.title,
        'news': query
    }
    return render(request, 'detailnews.html', context=context)

class NewsView(ListView):
    model = News
    template_name = "newslist.html"
    context_object_name = 'news'
    allow_empty = False

    def get_context_data(self, *, object_list=0, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'News'
        return context
    
    def get_queryset(self):
        return News.objects.filter(publicated=True)


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
