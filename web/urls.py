from django.urls import path

from .views import (
    home, registrate, sign_in, user_logout
)

urlpatterns = [
    path('', home, name='home'),
    path('registrate/', registrate, name='registrate'),
    path('login/', sign_in, name='login'),
    path('logout/', user_logout, name='logout')
]
