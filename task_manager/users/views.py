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


class UserFormUpdateView(View):

    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        user = User.objects.get(id=user_id)
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
            return redirect('users')
        return render(
            request,
            'users/update.html',
            {
                'form': form,
                'user_id': user_id
            }
        )


class UserFormDeleteView(View):

    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        user = User.objects.get(id=user_id)
        return render(
            request,
            'users/delete.html',
            {'user': user}
        )

    def post(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        user = User.objects.get(id=user_id)
        if user:
            user.delete()
        return redirect('users')
