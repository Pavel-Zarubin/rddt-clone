from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class UserRegisterForm(UserCreationForm):
    """
    Форма регистрации пользователя
    """
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'gender', 'email', 'password1', 'password2', 'inn']


class UserUpdateForm(forms.ModelForm):
    """
    Форма обновления профиля пользователя
    """
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'gender', 'email', 'inn', 'about_myself', 'image']

