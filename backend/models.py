from django.db import models

from . import enums

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=128)
    creation = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=256)
    description = models.CharField(max_length=512)
    creation = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(
        max_length=1,
        choices=enums.Priority.choices,
        default=enums.Priority.medium,
    )
    status = models.CharField(
        max_length=2,
        choices=enums.Status.choices,
        default=enums.Status.backlog,
    )
    update = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag, related_name="task")

    def __str__(self) -> str:
        return f"{self.title}|{self.status}"
