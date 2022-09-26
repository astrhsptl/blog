from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import News

class NewsForm(forms.ModelForm):

    class Meta:
        model = News
        fields = (
            'title', 'content', 'publicated'
        )


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Username',) #help_text='Enter your email',)# widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput())#attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = (
            'username', 
            'password', 
        )

class UserRegistrationForm(UserCreationForm):
    firstname = forms.CharField(label='Firstname',) 
    lastname = forms.CharField(label='Lastname',) 
    username = forms.CharField(label='Username',)# widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email',) #help_text='Enter your email',)# widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = (
            'firstname', 
            'lastname', 
            'username', 
            'email', 
        )