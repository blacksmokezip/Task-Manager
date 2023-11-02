from django.test import TestCase
from task_manager.labels.models import Label


class LabelCRUDTestCase(TestCase):
    fixtures = ['label.json']

    def setUp(self) -> None:
        self.label = Label.objects.get(pk=1)

    def test_create_label(self):
        self.assertEqual(self.label.name, 'Test')

    def test_read_label(self):
        label = Label.objects.get(name='Test')
        self.assertEqual(label, self.label)

    def test_update_label(self):
        self.label.name = 'Updated'
        self.label.save()
        updated_label = Label.objects.get(name='Updated')
        self.assertEqual(updated_label.name, 'Updated')

    def test_delete_label(self):
        self.label.delete()
        with self.assertRaises(Label.DoesNotExist):
            Label.objects.get(name='Updated')
