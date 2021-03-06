from typing import Union

from backend import enums
from backend import models as task_manager_models


def task_priority_validator(task_data: dict) -> bool:

    """
    Checks if a task with this priority already exists for the tag

    Returns:
        bool: True if priority available
    """
    if tags := task_data.get("tags"):
        return not (
            task_manager_models.Task.objects.prefetch_related("tags")
            .filter(tags__in=tags, priority=task_data["priority"])
            .exists()
        )
    return True


def task_status_validator(current_status: Union[enums.Status, str], new_status: Union[enums.Status, str]) -> bool:
    """
    Validates the correct sequence of statuses
    """
    status_list = list(enums.Status)
    return status_list[status_list.index(new_status) - 1] == current_status
