from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy


def index(request):
    return render(request, 'index.html')


class Login(LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))

    def get_success_url(self):
        messages.success(self.request, 'Вы залогинены')
        return reverse_lazy('main')


def logout_user(request):
    logout(request)
    messages.info(request, 'Вы разлогинены')
    return redirect('main')
