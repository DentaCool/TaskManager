from backend import models as task_manager_models
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from . import serializers as task_manager_serializers


class TagViewSet(ModelViewSet):
    queryset = task_manager_models.Tag.objects.all()
    serializer_class = task_manager_serializers.TagSerializer


class TaskViewSet(ModelViewSet):
    queryset = task_manager_models.Task.objects.all()
    serializer_class = task_manager_serializers.TaskSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["status", "priority"]
