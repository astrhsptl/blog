from django.urls import path

from .views import (
    home, registrate, sign_in, user_logout, 
    concrete_news, doesntexist, NewsView,
    editing_concrete_news, create_news
)

urlpatterns = [
    path('', home, name='home'),
    path('registrate/', registrate, name='registrate'),
    path('login/', sign_in, name='login'),
    path('logout/', user_logout, name='logout'),
    path('news/', NewsView.as_view(), name='news'),
    path('news/<int:news_id>/', concrete_news, name='datailnews'), 
    path('edit/<int:news_id>/', editing_concrete_news, name='editing'),
    path('creating/', create_news, name='creating')
]