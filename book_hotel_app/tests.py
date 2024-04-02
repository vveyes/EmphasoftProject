from django.test import TestCase
from django.contrib.auth import get_user_model

class CustomUserTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='tester2048',
            email='will@email.com',
            first_name = 'will',
            last_name='willer',
            password='12345',
        )
        self.assertEqual(user.username, 'tester2048')
        self.assertEqual(user.email, 'will@email.com')
        self.assertEqual(user.first_name, 'will')
        self.assertEqual(user.last_name, 'willer')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        user = User.objects.create_superuser(
            username='superuser',
            email='admin@email.com',
            first_name = 'admin',
            last_name='adminer',
            password='12345',
        )
        self.assertEqual(user.username, 'superuser')
        self.assertEqual(user.email, 'admin@email.com')
        self.assertEqual(user.first_name, 'admin')
        self.assertEqual(user.last_name, 'adminer')
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)