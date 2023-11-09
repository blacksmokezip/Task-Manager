from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView, ListView, CreateView, UpdateView

from task_manager.statuses.models import Status
from task_manager.statuses.forms import StatusForm
from django.utils.translation import gettext_lazy as _

from task_manager.mixins import AuthRequiredMixin, DeleteProtectionMixin


class IndexView(AuthRequiredMixin, ListView):

    template_name = 'statuses/index.html'
    model = Status
    context_object_name = 'statuses'


class StatusFormCreateView(AuthRequiredMixin, SuccessMessageMixin, CreateView):

    template_name = 'statuses/create.html'
    model = Status
    form_class = StatusForm
    success_url = reverse_lazy('statuses')
    success_message = _('Status successfully created')


class StatusFormUpdateView(AuthRequiredMixin, SuccessMessageMixin, UpdateView):

    template_name = 'statuses/update.html'
    model = Status
    form_class = StatusForm
    success_url = reverse_lazy('statuses')
    success_message = _('Status successfully changed')


class StatusFormDeleteView(
    AuthRequiredMixin,
    DeleteProtectionMixin,
    SuccessMessageMixin,
    DeleteView
):

    template_name = 'statuses/delete.html'
    model = Status
    success_url = reverse_lazy('statuses')
    success_message = _('Status successfully deleted')
    protected_message = _('It is not possible to delete a status '
                          'because it is in use')
    protected_url = reverse_lazy('statuses')
    extra_context = {
        'title': _('Delete status'),
        'button_text': _('Yes, delete'),
    }
