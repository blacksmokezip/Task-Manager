from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from task_manager.users.forms import UserCreateForm


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
            return redirect('users')
        return render(request, 'users/create.html', {'form': form})
