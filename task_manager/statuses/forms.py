from django import forms
from task_manager.statuses.models import Status


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ('name',)
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Имя'}),
        }
        labels = {
            'name': 'Имя',
        }
