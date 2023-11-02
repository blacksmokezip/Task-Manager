from django_filters import FilterSet, BooleanFilter, CharFilter, ChoiceFilter, ModelChoiceFilter
from django import forms
from django.utils.translation import gettext_lazy as _

from task_manager.tasks.models import Task
from task_manager.labels.models import Label


class TaskFilter(FilterSet):

    labels = ModelChoiceFilter(
        queryset=Label.objects.all(),
        label='Метка'
    )

    own_tasks = BooleanFilter(
        label=_('Только свои задачи'),
        widget=forms.CheckboxInput,
        method='get_own_tasks',
    )

    def get_own_tasks(self, queryset, name, value):
        if value:
            user = self.request.user
            return queryset.filter(author=user)
        return queryset

    class Meta:

        model = Task
        fields = ['status', 'executor']
