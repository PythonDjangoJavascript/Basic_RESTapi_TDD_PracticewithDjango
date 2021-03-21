from django.test import TestCase
from django.contrib.auth import get_user_model

from core.models import ProfileFeedItem


class ModelTest(TestCase):
    """Tests User Database"""

    def test_create_user_with_email_successful(self):
        """Test creating user with email successful and
        don't have super access"""

        email = "test@email.com"
        password = "testpass123"
        name = "testName"
        user = get_user_model().objects.create_user(
            email=email,
            name=name,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        self.assertEqual(user.name, name)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_neew_user_email_normalized(self):
        """Test user email normalized function is working"""

        email = "test@GMAIL.COM"
        user = get_user_model().objects.create_user(
            email=email,
            name="Test Name",
            password="TestPass123"
        )

        self.assertEqual(user.email, email.lower())

    def test_none_email_valuse_error(self):
        """test if without email user can be created"""

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "name", "apass12")

    def test_creat_superuser(self):
        """Test creating a superuser and is stuff and superuser"""

        user = get_user_model().objects.create_superuser(
            email="super@user.com",
            name="suer user",
            password="superpass123"
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_user_status_updated(self):
        """Test user status updated successfully"""

        user = get_user_model().objects.create_user(
            email="test@user.com",
            name="test user",
            password="testuserpass"
        )

        status_text = "Hello World"

        ProfileFeedItem.objects.create(
            user_profile=user,
            status_text=status_text
        )

        self.assertEqual(user.profile_feeds.count(), 1)
