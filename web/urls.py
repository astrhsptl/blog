from django.urls import path

from .views import (
    home, registrate
)

urlpatterns = [
    path('', home, name='home'),
    path('registrate/', registrate, name='registrate'),
]
