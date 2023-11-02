from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.utils.translation import gettext_lazy as _
from django.contrib.messages.views import SuccessMessageMixin
from django_filters.views import FilterView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User

from task_manager.mixins import AuthRequiredMixin, AuthorDeletionMixin
from task_manager.tasks.models import Task
from task_manager.tasks.forms import TaskForm
from task_manager.tasks.filters import TaskFilter


class TasksListView(LoginRequiredMixin, FilterView):

    login_url = 'login'

    template_name = 'tasks/index.html'
    model = Task
    filterset_class = TaskFilter
    context_object_name = 'tasks'
    extra_context = {
        'title': 'Задачи',
        'button_text': 'Показать'
    }


class TaskDetailView(AuthRequiredMixin, DetailView):

    login_url = 'login'

    template_name = 'tasks/show.html'
    model = Task
    context_object_name = 'task'
    extra_context = {
        'title': 'Просмотр задачи'
    }


class TaskCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):

    login_url = 'login'

    template_name = 'tasks/create.html'
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('tasks')
    success_message = 'Задача успешно создана'
    extra_context = {
        'title': 'Создать задачу',
        'button_text': 'Создать',
    }

    def form_valid(self, form):
        user = self.request.user
        form.instance.author = User.objects.get(pk=user.pk)
        return super().form_valid(form)


class TaskUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):

    login_url = 'login'

    template_name = 'tasks/update.html'
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('tasks')
    success_message = 'Задача успешно изменена'
    extra_context = {
        'title': 'Изменение задачи',
        'button_text': 'Изменить',
    }


class TaskDeleteView(AuthRequiredMixin, AuthorDeletionMixin, SuccessMessageMixin, DeleteView):

    login_url = 'login'

    template_name = 'tasks/delete.html'
    model = Task
    success_url = reverse_lazy('tasks')
    success_message = 'Задача успешно удалена'
    author_message = 'Задачу может удалить только ее автор'
    author_url = reverse_lazy('tasks')
    extra_context = {
        'title': 'Удаление задачи',
        'button_text': 'Да, удалить',
    }
