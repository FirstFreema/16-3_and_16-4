from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    """
    Форма для создания нового пользователя.
    """
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1',
                  'password2', 'age', 'bio', 'avatar', 'birth_date']

class CustomUserChangeForm(UserChangeForm):
    """
    Форма для изменения данных пользователя.
    """
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'age', 'bio', 'avatar', 'birth_date']

class CustomAuthenticationForm(AuthenticationForm):
    """
    Форма для входа в аккаунт.
    """
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'User name'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'password'}))

