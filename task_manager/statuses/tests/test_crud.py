from django.test import TestCase
from task_manager.statuses.models import Status


class StatusCRUDTestCase(TestCase):
    fixtures = ['status.json']

    def setUp(self) -> None:
        self.status = Status.objects.get(pk=1)

    def test_create_status(self):
        self.assertEqual(self.status.name, 'Started')

    def test_read_status(self):
        status = Status.objects.get(name='Started')
        self.assertEqual(status, self.status)

    def test_update_status(self):
        self.status.name = 'Finished'
        self.status.save()
        updated_status = Status.objects.get(name='Finished')
        self.assertEqual(updated_status.name, 'Finished')

    def test_delete_status(self):
        self.status.delete()
        with self.assertRaises(Status.DoesNotExist):
            Status.objects.get(name='Finished')
