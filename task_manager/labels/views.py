from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.utils.translation import gettext_lazy as _
from django.contrib.messages.views import SuccessMessageMixin
from django.views import View

from task_manager.mixins import AuthRequiredMixin, AuthorDeletionMixin, DeleteProtectionMixin
from task_manager.labels.models import Label
from task_manager.labels.forms import LabelForm


class LabelsListView(AuthRequiredMixin, ListView):

    template_name = 'labels/index.html'
    model = Label
    context_object_name = 'labels'
    extra_context = {
        'title': 'Метки',
    }


class LabelsCreateView(AuthRequiredMixin, SuccessMessageMixin, CreateView):

    template_name = 'labels/create.html'
    model = Label
    form_class = LabelForm
    success_url = reverse_lazy('labels')
    success_message = 'Метка успешно создана'
    extra_context = {
        'title': 'Создать метку',
        'button_text': 'Создать',
    }


class LabelsUpdateView(AuthRequiredMixin, SuccessMessageMixin, UpdateView):

    template_name = 'labels/update.html'
    model = Label
    form_class = LabelForm
    success_url = reverse_lazy('labels')
    success_message = 'Метка успешно изменена'
    extra_context = {
        'title': 'Изменение метки',
        'button_text': 'Изменить',
    }


class LabelsDeleteView(AuthRequiredMixin, DeleteProtectionMixin, SuccessMessageMixin, DeleteView):

    template_name = 'labels/delete.html'
    model = Label
    success_url = reverse_lazy('labels')
    success_message = 'Метка успешно удалена'
    protected_message = 'Невозможно удалить метку, потому что она используется'
    protected_url = reverse_lazy('labels')
    extra_context = {
        'title': 'Удаление метки',
        'button_text': 'Да, удалить',
    }
