from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating new user with email address"""

        email = 'test@test.com'
        password = 'test123'

        user = get_user_model().objects.create_user(email=email, password=password)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_email_normalize(self):
        email = 'test@test.com'
        user = get_user_model().objects.create_user(email, 'test')

        self.assertEqual(user.email, email)

    def test_create_user_without_user(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, '123')

    def test_create_new_super_user(self):
        user = get_user_model().objects.create_superuser('test@asd.com', '123')

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
