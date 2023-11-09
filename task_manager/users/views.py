from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from task_manager.users.models import User
from django.views.generic import DeleteView, UpdateView, CreateView, ListView
from django.utils.translation import gettext_lazy as _

from task_manager.mixins import DeleteProtectionMixin, \
    UserPermissionMixin, AuthRequiredMixin
from task_manager.users.forms import UserCreateForm


class IndexView(ListView):

    template_name = 'users/index.html'
    model = User
    context_object_name = 'users'


class UserFormCreateView(SuccessMessageMixin, CreateView):

    template_name = 'users/create.html'
    model = User
    form_class = UserCreateForm
    success_url = reverse_lazy('login')
    success_message = _('User is successfully registered')


class UserFormUpdateView(AuthRequiredMixin, UserPermissionMixin,
                     SuccessMessageMixin, UpdateView):

    template_name = 'users/update.html'
    model = User
    form_class = UserCreateForm
    success_url = reverse_lazy('users')
    success_message = _('User is successfully updated')
    permission_message = _('You have no rights to change another user.')
    permission_url = reverse_lazy('users')


class UserFormDeleteView(AuthRequiredMixin, UserPermissionMixin,
                         DeleteProtectionMixin, SuccessMessageMixin,
                         DeleteView):

    template_name = 'users/delete.html'
    model = User
    success_url = reverse_lazy('users')
    success_message = _('User is successfully deleted')
    permission_message = _('You have no rights to change another user.')
    permission_url = reverse_lazy('users')
    protected_message = \
        _('Unable to delete a user because he is being used')
    protected_url = reverse_lazy('users')
