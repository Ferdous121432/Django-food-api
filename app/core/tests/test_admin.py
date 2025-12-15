"""
Tests for admin modifications.
"""

from django.test import TestCase  # noqa
from django.contrib.auth import get_user_model  # noqa
from django.urls import reverse  # noqa
from django.test import Client  # noqa


class AdminSiteTests(TestCase):
    """Tests for admin modifications."""

    def setUp(self):
        """Set up test client and create a superuser."""
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='f@ff.com',
            password='testpass123'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='user@example.com',
            password='userpass123'
        )

    def test_users_listed(self):
        """Test that users are listed on user page."""
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_edit_user_page(self):
        """Test that the edit user page works."""
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """Test that the create user page works."""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
