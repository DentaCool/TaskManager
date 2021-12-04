from backend import models as task_manager_models
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from . import serializers as task_manager_serializers


class TagViewSet(ModelViewSet):
    queryset = task_manager_models.Tag.objects.all()
    serializer_class = task_manager_serializers.TagSerializer
    serializer_classes = {"list": task_manager_serializers.TagListSerializer}

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.serializer_class)


class TaskViewSet(ModelViewSet):
    queryset = task_manager_models.Task.objects.all()
    serializer_class = task_manager_serializers.TaskSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["status", "priority"]
