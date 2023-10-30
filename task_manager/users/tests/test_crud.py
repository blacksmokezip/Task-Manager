from django.test import TestCase
from django.contrib.auth.models import User


class UserCRUDTestCase(TestCase):
    fixtures = ['user.json']

    def setUp(self) -> None:
        self.user = User.objects.get(pk=1)

    def test_create_user(self):
        self.assertEqual(self.user.username, 'testuser')

    def test_read_user(self):
        user = User.objects.get(username='testuser')
        self.assertEqual(user, self.user)

    def test_update_user(self):
        self.user.first_name = 'Jimmy'
        self.user.last_name = 'Page'
        self.user.save()
        updated_user = User.objects.get(username='testuser')
        self.assertEqual(updated_user.first_name, 'Jimmy')
        self.assertEqual(updated_user.last_name, 'Page')

    def test_delete_user(self):
        self.user.delete()
        with self.assertRaises(User.DoesNotExist):
            User.objects.get(username='testuser')
