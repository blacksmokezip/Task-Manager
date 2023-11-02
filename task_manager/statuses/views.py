from django.shortcuts import render, redirect
from django.views import View
from task_manager.statuses.models import Status
from task_manager.statuses.forms import StatusForm
from django.contrib import messages

from task_manager.mixins import AuthRequiredMixin


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
            messages.success(request, 'Статус успешно создан')
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
            messages.success(request, 'Статус успешно изменен')
            return redirect('statuses')
        return render(
            request,
            'statuses/update.html',
            {
                'form': form,
                'status_id': status_id
            }
        )


class StatusFormDeleteView(AuthRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        status_id = kwargs.get('id')
        status = Status.objects.get(id=status_id)
        return render(
            request,
            'statuses/delete.html',
            {'status': status}
        )

    def post(self, request, *args, **kwargs):
        status_id = kwargs.get('id')
        status = Status.objects.get(id=status_id)
        if status:
            status.delete()
        messages.success(request, 'Статус успешно удален')
        return redirect('statuses')
