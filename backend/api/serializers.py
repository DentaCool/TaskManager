from backend import models as task_manager_models
from backend.validators import task_priority_validator, task_status_validator
from rest_framework import serializers


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = task_manager_models.Task
        fields = "__all__"

    def create(self, validated_data):
        if task_priority_validator(validated_data):
            return super().create(validated_data)
        raise serializers.ValidationError({"error": "Task with same priority already exists!"})

    def update(self, instance, validated_data):
        if task_status_validator(instance.status, validated_data["status"]):
            return super().update(instance, validated_data)
        raise serializers.ValidationError({"error": "Wrong status ordering!"})


class TagListSerializer(serializers.ModelSerializer):
    class Meta:
        model = task_manager_models.Tag
        fields = (
            "id",
            "name",
        )


class TagSerializer(TagListSerializer):
    tasks = TaskSerializer(many=True)

    class Meta:
        model = task_manager_models.Tag
        fields = "__all__"
