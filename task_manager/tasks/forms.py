from django import forms
from task_manager.tasks.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'description', 'status', 'executor',)
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Имя'}),
            'description': forms.Textarea(attrs={'placeholder': 'Описание'}),
        }
        labels = {
            'name': 'Имя',
            'description': 'Описание',
            'status': 'Статус',
            'executor': 'Исполнитель',
        }
