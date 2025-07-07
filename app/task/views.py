"""
Views for the task APIs.
"""
from drf_spectacular.utils import (
    extend_schema_view,
    extend_schema,
    OpenApiParameter,
    OpenApiTypes,
)
from rest_framework import (
    viewsets,
    generics
)
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Task
from task import serializers


@extend_schema_view(
    list=extend_schema(
        parameters=[
            OpenApiParameter(
                name='description',
                type=OpenApiTypes.STR,
                description='Filter tasks by description (partial match)',
                required=False,
            ),
            OpenApiParameter(
                name='status',
                type=OpenApiTypes.STR,
                description='Filter tasks by status',
                required=False,
            ),
            OpenApiParameter(
                name='user',
                type=OpenApiTypes.STR,
                description='Filter tasks by assigned user name',
                required=False,
            ),
            OpenApiParameter(
                name='name',
                type=OpenApiTypes.STR,
                description='Filter tasks by name of task',
                required=False,
            ),
            OpenApiParameter(
                name='id',
                type=OpenApiTypes.STR,
                description='Filter task by id',
                required=False,
            )
        ]
    )
)
class TaskViewSet(viewsets.ModelViewSet):
    """View for manage task APIs."""
    serializer_class = serializers.TaskDetailSerializer
    queryset = Task.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Retrieve tasks for authenticated user, with optional filters."""
        queryset = self.queryset.all()

        description = self.request.query_params.get('description')
        if description:
            queryset = queryset.filter(description__icontains=description)

        status = self.request.query_params.get('status')
        if status:
            queryset = queryset.filter(status=status)

        user_name = self.request.query_params.get('user')
        if user_name:
            queryset = queryset.filter(user__name__icontains=user_name)

        task_name = self.request.query_params.get('name')
        if task_name:
            queryset = queryset.filter(name__icontains=task_name)

        task_id = self.request.query_params.get('id')
        if task_id:
            queryset = queryset.filter(id=task_id)

        return queryset

    def get_serializer_class(self):
        """Return the serializer for request."""
        if self.action == 'list':
            return serializers.TaskSerializer

        return self.serializer_class

    def perform_create(self, serializer):
        user = serializer.validated_data.get('user')
        if user is None:
            serializer.save(user=self.request.user)
        else:
            serializer.save()

class TaskHistoryView(generics.ListAPIView):
    serializer_class = serializers.TaskHistorySerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        task_id = self.kwargs['pk']
        return Task.history.filter(id=task_id).order_by('-history_date')
