from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class AuthSchema(BaseModel):
    username: str
    password: str


class TokenPayloadSchema(BaseModel):
    user_id: UUID
    created_at: datetime


class TaskCreateSchema(BaseModel):
    name: str
    description: str | None = None


class TaskUpdateSchema(BaseModel):
    name: str
    description: str | None = None


class TaskStatusUpdateSchema(BaseModel):
    is_completed: bool
