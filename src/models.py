from enum import StrEnum

from tortoise import fields
from tortoise.models import Model


class User(Model):
    id = fields.UUIDField(pk=True)  # noqa: A003
    username = fields.CharField(unique=True, max_length=20)
    password = fields.CharField(max_length=100)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = 'users'


class Task(Model):
    class Status(StrEnum):
        NEW = 'new'
        COMPLETED = 'completed'

    id = fields.UUIDField(pk=True)  # noqa: A003
    user = fields.ForeignKeyField('models.User', related_name='tasks', on_delete=fields.CASCADE)
    name = fields.CharField(max_length=100, unique=True)
    status = fields.CharEnumField(Status)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = 'tasks'
