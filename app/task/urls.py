"""
URL mappings for the taks app.
"""
from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter

from task import views


router = DefaultRouter()
router.register('tasks', views.TaskViewSet)

app_name = 'task'

urlpatterns = [
    path('',include(router.urls)),
    path('tasks/<int:pk>/history/', views.TaskHistoryView.as_view(), name='task-history'),
]