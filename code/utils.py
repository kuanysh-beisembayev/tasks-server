from typing import Mapping

from code.models import Task


def serialize_task(task: Task) -> Mapping:
    return {
        'id': str(task.id),
        'name': task.name,
        'status': task.status,
    }
