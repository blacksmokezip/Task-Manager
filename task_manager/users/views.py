from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from task_manager.users.models import User
from django.views.generic import DeleteView
from django.utils.translation import gettext_lazy as _

from task_manager.mixins import DeleteProtectionMixin, \
    UserPermissionMixin, AuthRequiredMixin
from task_manager.users.forms import UserCreateForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(View):

    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        return render(request, 'users/index.html', context={
            'users': users,
        })


class UserFormCreateView(View):

    def get(self, request, *args, **kwargs):
        form = UserCreateForm()
        return render(request, 'users/create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _('User is successfully registered'))
            return redirect('login')
        return render(request, 'users/create.html', {'form': form})


class UserFormUpdateView(LoginRequiredMixin, View):

    login_url = "login"

    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        user = User.objects.get(id=user_id)
        if request.user != user and not request.user.is_superuser:
            messages.error(
                request,
                _('You have no rights to change another user.')
            )
            return redirect('users')
        form = UserCreateForm(instance=user)
        return render(
            request,
            'users/update.html',
            {
                'form': form,
                'user_id': user_id
            }
        )

    def post(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        user = User.objects.get(id=user_id)
        form = UserCreateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, _('User is successfully updated'))
            return redirect('users')
        return render(
            request,
            'users/update.html',
            {
                'form': form,
                'user_id': user_id
            }
        )


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
