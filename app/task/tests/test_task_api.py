"""
Tests for task APIs.
"""

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Task

from task.serializers import (
    TaskSerializer,
    TaskDetailSerializer,
)


TASK_URL = reverse('task:task-list')


def detail_url(task_id):
    """Create and return a task detail URL."""
    return reverse('task:task-detail', args=[task_id])


def create_task(user, **params):
    """Create and return a task."""
    defaults = {
        'name': 'Task name',
        'description': 'Sample description',
        'status': 'Nowy',
    }
    defaults.update(params)

    task = Task.objects.create(user=user, **defaults)
    return task


class PublicTaskAPITests(TestCase):
    """Test unauthenticated API requests."""

    def setUp(self):
        self.client = APIClient()

    def test_auth_required(self):
        """Test auth is required to call API."""
        res = self.client.get(TASK_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateRecipeApiTests(TestCase):
    """Test authenticated API requests."""

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            'user@example.com',
            'testpass123',
            name='user1'  # <-- unikalny name
        )
        self.client.force_authenticate(self.user)

    def test_get_task_detail(self):
        """Test get task detail."""
        task = create_task(user=self.user)

        url = detail_url(task.id)
        res = self.client.get(url)

        serializer = TaskDetailSerializer(task)
        self.assertEqual(res.data, serializer.data)

    def test_create_task(self):
        """Test creating a task."""
        payload = {
            'name': 'Sample Name',
            'description': 'Sample Description',
            'status': 'nowy',
        }
        res = self.client.post(TASK_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        task = Task.objects.get(id=res.data['id'])
        self.assertEqual(task.name, payload['name'])
        self.assertEqual(task.description, payload['description'])
        self.assertEqual(task.status, payload['status'])
        self.assertEqual(task.user, self.user)

    def test_filter_by_names(self):
        """Test filtering task by description"""
        r1 = create_task(user=self.user, description='zadanie od mamy')
        r2 = create_task(user=self.user, description='zadanie od taty')
        filter = 'mamy'
        params = {'description': f'{filter}'}
        res = self.client.get(TASK_URL, params)

        s1 = TaskSerializer(r1)
        s2 = TaskSerializer(r2)
        self.assertIn(s1.data, res.data)
        self.assertNotIn(s2.data, res.data)

    def test_filter_by_status(self):
        """Test filtering task by status"""
        r1 = create_task(user=self.user, description='zadanie od mamy', status='w_trakcie')
        r2 = create_task(user=self.user, description='zadanie od taty', status='nowy')
        filter = 'nowy'
        params = {'status': f'{filter}'}
        res = self.client.get(TASK_URL, params)

        s1 = TaskSerializer(r1)
        s2 = TaskSerializer(r2)
        self.assertNotIn(s1.data, res.data)
        self.assertIn(s2.data, res.data)