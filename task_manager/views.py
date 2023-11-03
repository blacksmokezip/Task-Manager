from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _


def index(request):
    return render(request, 'index.html')


class UserLoginView(SuccessMessageMixin, LoginView):
    template_name = 'login.html'
    form_class = AuthenticationForm
    next_page = reverse_lazy('main')
    success_message = _('You are logged in')
    extra_context = {
        'title': _('Login'),
        'button_text': _('Enter'),
    }


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('main')
    success_message = _('You are logged out')

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, _('You are logged out'))
        return super().dispatch(request, *args, **kwargs)