from django.test import TestCase
from django.contrib.auth.models import User


class UserCRUDTestCase(TestCase):
    fixtures = ['user.json']

    def setUp(self):
        # Создаем тестового пользователя
        self.user = User.objects.get(pk=1)

    def test_create_user(self):
        # Проверяем, что пользователь был успешно создан
        self.assertEqual(self.user.username, 'testuser')

    def test_read_user(self):
        # Проверяем, что пользователь существует в базе данных
        user = User.objects.get(username='testuser')
        self.assertEqual(user, self.user)

    def test_update_user(self):
        # Изменяем данные пользователя и проверяем, что изменения были сохранены
        self.user.first_name = 'Jimmy'
        self.user.last_name = 'Page'
        self.user.save()
        updated_user = User.objects.get(username='testuser')
        self.assertEqual(updated_user.first_name, 'Jimmy')
        self.assertEqual(updated_user.last_name, 'Page')

    def test_delete_user(self):
        # Удаляем пользователя и проверяем, что он больше не существует в базе данных
        self.user.delete()
        with self.assertRaises(User.DoesNotExist):
            User.objects.get(username='testuser')
