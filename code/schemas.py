from pydantic import BaseModel

from code.models import Task


class TaskCreateSchema(BaseModel):
    name: str
    status: Task.Status


class TaskUpdateSchema(BaseModel):
    name: str
    status: Task.Status
