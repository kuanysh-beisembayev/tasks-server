from enum import StrEnum

from tortoise import fields
from tortoise.models import Model


class Task(Model):
    class Status(StrEnum):
        NEW = 'new'
        COMPLETED = 'completed'

    id = fields.UUIDField(pk=True)  # noqa: A003
    name = fields.CharField(max_length=100, unique=True)
    status = fields.CharEnumField(Status)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = 'tasks'
