from django.test import TestCase
from task_manager.tasks.models import Task
from task_manager.statuses.models import Status
from django.contrib.auth.models import User


class TaskCRUDTestCase(TestCase):
    fixtures = ['task.json', 'status.json', 'user.json']

    def setUp(self) -> None:
        self.task = Task.objects.get(pk=1)
        self.status = Status.objects.get(pk=1)
        self.user = User.objects.get(pk=1)

    def test_create_task(self):
        self.assertEqual(self.task.name, 'Do')

    def test_read_task(self):
        task = Task.objects.get(name='Do')
        self.assertEqual(task, self.task)

    def test_update_task(self):
        self.task.description = 'Updated'
        self.task.save()
        updated_task = Task.objects.get(name='Do')
        self.assertEqual(updated_task.description, 'Updated')

    def test_delete_task(self):
        self.task.delete()
        with self.assertRaises(Task.DoesNotExist):
            Task.objects.get(name='Do')
