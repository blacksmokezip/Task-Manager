from django.test import TestCase
from task_manager.users.models import User
from django.urls import reverse_lazy

from task_manager.tasks.models import Task
from task_manager.statuses.models import Status
from task_manager.labels.models import Label


class TaskFilterTestCase(TestCase):
    fixtures = ['task.json', 'status.json', 'user.json', 'label.json']

    def setUp(self):
        self.task = Task.objects.get(pk=1)
        self.status = Status.objects.get(pk=1)
        self.user = User.objects.get(pk=1)
        self.label = Label.objects.get(pk=1)

        self.client.force_login(self.user)

    def test_filter_tasks_by_status(self) -> None:
        response = self.client.get(
            reverse_lazy('tasks'),
            {'status': self.status.pk}
        )

        self.assertEqual(response.context['tasks'].count(), 1)
        self.assertContains(response, self.task.name)

    def test_filter_tasks_by_executor(self) -> None:
        response = self.client.get(
            reverse_lazy('tasks'),
            {'executor': self.user.pk}
        )

        self.assertEqual(response.context['tasks'].count(), 1)
        self.assertContains(response, self.task.name)

    def test_filter_tasks_by_label(self) -> None:
        response = self.client.get(
            reverse_lazy('tasks'),
            {'labels': self.label.pk}
        )

        self.assertEqual(response.context['tasks'].count(), 1)
        self.assertContains(response, self.task.name)

    def test_filter_tasks_by_own_tasks(self) -> None:
        response = self.client.get(
            reverse_lazy('tasks'),
            {'own_tasks': 'on'}
        )

        self.assertEqual(response.context['tasks'].count(), 1)
        self.assertContains(response, self.task.name)
