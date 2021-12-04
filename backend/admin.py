from django.contrib import admin

from . import models as task_manager_models

# Register your models here.


@admin.register(task_manager_models.Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["__str__"]


@admin.register(task_manager_models.Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["__str__"]
