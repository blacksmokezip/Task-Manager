from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# from django.forms import TextInput, PasswordInput, CharField, ModelForm
# from django.core.validators import MinLengthValidator
# from django import forms


# class UserCreateForm(ModelForm):
#     password1 = CharField(
#         label="Пароль",
#         widget=PasswordInput(attrs={
#             'placeholder': 'Пароль',
#             'class': 'form-control'
#         }),
#     )
#     password2 = CharField(
#         label="Подтверждение пароля",
#         widget=PasswordInput(attrs={
#             'placeholder': 'Подтверждение пароля',
#             'class': 'form-control'
#         }),
#     )
#
#     class Meta:
#         model = User
#         fields = ('first_name', 'last_name', 'username', 'password1', 'password2')
#         widgets = {
#             'first_name': TextInput(attrs={
#                 'placeholder': 'Имя',
#                 'class': 'form-control'
#             }),
#             'last_name': TextInput(attrs={
#                 'placeholder': 'Фамилия',
#                 'class': 'form-control'
#             }),
#             'username': TextInput(attrs={
#                 'placeholder': 'Имя пользователя',
#                 'class': 'form-control'
#             })
#         }
#
#     def clean_password2(self):
#         password1 = self.cleaned_data.get("password1")
#         password2 = self.cleaned_data.get("password2")
#
#         if password1 and password2 and password1 != password2:
#             raise forms.ValidationError("Введенные пароли не совпадают.")
#
#         if len(password1) < 3 or len(password2) < 3:
#             raise forms.ValidationError("Введённый пароль слишком короткий. Он должен содержать как минимум 3 символа.")
#
#         return password2

class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2')