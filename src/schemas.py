from datetime import datetime
from uuid import UUID

from pydantic import BaseModel

from src.models import Task


class AuthSchema(BaseModel):
    username: str
    password: str


class TokenPayloadSchema(BaseModel):
    user_id: UUID
    created_at: datetime


class TaskCreateSchema(BaseModel):
    name: str
    status: Task.Status


class TaskUpdateSchema(BaseModel):
    name: str
    status: Task.Status
