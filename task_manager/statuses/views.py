from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DeleteView

from task_manager.statuses.models import Status
from task_manager.statuses.forms import StatusForm
from django.contrib import messages
from django.utils.translation import gettext_lazy as _

from task_manager.mixins import AuthRequiredMixin, DeleteProtectionMixin


class IndexView(AuthRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        statuses = Status.objects.all()
        return render(request, 'statuses/index.html', context={
            'statuses': statuses,
        })


class StatusFormCreateView(AuthRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        form = StatusForm()
        return render(request, 'statuses/create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = StatusForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _('Status successfully created'))
            return redirect('statuses')
        return render(request, 'statuses/create.html', {'form': form})


class StatusFormUpdateView(AuthRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        status_id = kwargs.get('id')
        status = Status.objects.get(id=status_id)
        form = StatusForm(instance=status)
        return render(
            request,
            'statuses/update.html',
            {
                'form': form,
                'status_id': status_id
            }
        )

    def post(self, request, *args, **kwargs):
        status_id = kwargs.get('id')
        status = Status.objects.get(id=status_id)
        form = StatusForm(request.POST, instance=status)
        if form.is_valid():
            form.save()
            messages.success(request, _('Status successfully changed'))
            return redirect('statuses')
        return render(
            request,
            'statuses/update.html',
            {
                'form': form,
                'status_id': status_id
            }
        )


class StatusFormDeleteView(AuthRequiredMixin,
                       DeleteProtectionMixin,
                       SuccessMessageMixin,
                       DeleteView):

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
