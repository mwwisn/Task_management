"""
Tests for models.
"""
from decimal import Decimal

from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


class ModelTests(TestCase):
    """Test models."""

    def test_create_user_with_email_succesful(self):
        """Test creating a user with an email is succesful."""
        email = 'test@example.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
            name='user_unique_1'
        )

        self.assertEqual(user.email, email)
        self.assertEqual(user.check_password(password), True)

    def test_new_user_normalized(self):
        """Test email is normalized for new users."""
        sample_emails = [
            ['test1@EXAMPLE.COM','test1@example.com'],
            ['Test2@Example.com','Test2@example.com'],
            ['TEST3@EXAMPLE.COM','TEST3@example.com'],
            ['test4@example.COM','test4@example.com'],
        ]
        counter = 1
        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(
                email,
                'sample123',
                name=f'unique_name_{counter}'  # <-- unikalne name w pętli
            )
            self.assertEqual(user.email, expected)
            counter += 1

    def test_new_user_without_email_raises_error(self):
        """Test that creating a user without an email raises a ValueError."""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                '',
                'test123',
                name='unique_name_no_email'  # <-- też dodaj name
            )
    def test_create_task(self):
        """Test creating a task is succesfull."""
        user = get_user_model().objects.create_user(
            'test@example.com',
            'testpass123',
            name='user_unique_for_task'
        )
        task = models.Task.objects.create(
            user=user,
            name='Task Example',
            description='Task description',
            status='Nowy',
        )

        self.assertEqual(str(task), task.name)
