"""
Tests for models.
"""

from django.test import TestCase  # noqa
from django.contrib.auth import get_user_model  # noqa
from unittest.mock import patch  # noqa


class ModelTests(TestCase):
    """Tests for models."""

    def test_create_user_with_email_successful(self):
        """Test creating a user with an email is successful."""
        email = 'test@example.com'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(

            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized."""
        sample_emails = [
            ['Test@EXAMPLE.com', 'test@example.com'],
            ['Another@Example.COM', 'another@example.com'],
            ['USER@DOMAIN.COM', 'user@domain.com'],
        ]

        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(
                email=email,
                password='test123'
            )
            self.assertEqual(user.email, expected)

    def test_create_user_no_email_raises_error(self):
        """Test creating a user with no email raises a ValueError."""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(email='', password='test123')

    def test_create_superuser(self):
        """Test creating a superuser."""
        user = get_user_model().objects.create_superuser(
            email='superuser@example.com',
            password='superpass123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_create_superuser(self):
        """Test creating a superuser."""
        user = get_user_model().objects.create_superuser(
            email='superuser@example.com',
            password='superpass123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
