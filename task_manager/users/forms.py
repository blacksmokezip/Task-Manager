from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import TextInput, PasswordInput, CharField


class UserCreateForm(UserCreationForm):
    password1 = CharField(label="Пароль", widget=PasswordInput(attrs={
                'placeholder': 'Пароль',
                'class': 'form-control'
            }))
    password2 = CharField(label="Повтор пароля", widget=PasswordInput(attrs={
        'placeholder': 'Подтверждение пароля',
        'class': 'form-control'
    }))

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
            })
        }
