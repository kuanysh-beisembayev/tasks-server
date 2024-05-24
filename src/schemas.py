from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, constr


class AuthSchema(BaseModel):
    username: str
    password: str


class TokenPayloadSchema(BaseModel):
    user_id: UUID
    created_at: datetime


class TaskSchema(BaseModel):
    name: constr(min_length=1, max_length=100)
    is_important: bool


class TaskStatusUpdateSchema(BaseModel):
    is_completed: bool
