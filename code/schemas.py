from pydantic import BaseModel

from code.models import Task


class TaskCreateSchema(BaseModel):
    name: str


class TaskUpdateSchema(BaseModel):
    name: str
    description: str | None
    status: Task.Status
