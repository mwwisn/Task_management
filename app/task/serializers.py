"""
Serializers for task APIs.
"""
from django.contrib.auth import get_user_model
from rest_framework import serializers

from core.models import Task

User = get_user_model()


class TaskSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field='name',  # szukamy usera po emailu
        queryset=User.objects.all(),
        required=False,
        allow_null=True,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Pokazuje nazwę użytkownika w dropdownie zamiast ID
        self.fields['user'].label = 'Przypisany użytkownik'
        self.fields['user'].display_value = lambda instance: instance.name or instance.email

    class Meta:
        model = Task
        fields = ['id', 'name', 'description', 'status', 'user']
        read_only_fields = ['id']
        extra_kwargs = {
            'user': {'required': False, 'allow_null': True},
        }

class TaskHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Task.history.model
        fields = '__all__'

class TaskDetailSerializer(TaskSerializer):
    """Serializer for task detail view."""

    class Meta(TaskSerializer.Meta):
        fields = TaskSerializer.Meta.fields