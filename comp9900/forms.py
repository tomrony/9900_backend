from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username',
                  'password1',
                  'password2',
                  'groups']

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=20, required=True)
    password = forms.CharField(required=True)
    class Meta:
        model = User
        fields = ['username', 'password']
