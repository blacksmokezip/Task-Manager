from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import TextInput, PasswordInput


class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2')
        widgets = {
            'first_name': TextInput(attrs={
                'placeholder': 'Имя',
                'class': 'form-control'
            }),
            'last_name': TextInput(attrs={
                'placeholder': 'Фамилия',
                'class': 'form-control'
            }),
            'username': TextInput(attrs={
                'placeholder': 'Имя пользователя',
                'class': 'form-control'
            }),
            'password1': PasswordInput(attrs={
                'placeholder': 'Пароль',
                'class': 'form-control'
            }),
            'password2': PasswordInput(attrs={
                'placeholder': 'Подтверждение пароля',
                'class': 'form-control'
            })
        }
