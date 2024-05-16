from datetime import datetime, timedelta, UTC
from typing import Mapping
from uuid import UUID

from jwt import decode, encode, InvalidTokenError
from passlib.context import CryptContext
from pydantic import ValidationError

from src.config import settings
from src.models import Task, User
from src.schemas import TokenPayloadSchema

ACCESS_TOKEN_TTL = timedelta(days=7)

crypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def serialize_task(task: Task) -> Mapping:
    completed_at = task.completed_at

    if completed_at:
        completed_at = completed_at.isoformat()

    return {
        'id': str(task.id),
        'name': task.name,
        'description': task.description,
        'created_at': task.created_at.isoformat(),
        'completed_at': completed_at,
        'is_important': task.is_important,
    }


def get_password_hash(password: str) -> str:
    return crypt_context.hash(password)


def password_matches(password: str, password_hash: str) -> bool:
    return crypt_context.verify(password, password_hash)


def create_access_token(user_id: UUID) -> str:
    payload = {
        'user_id': str(user_id),
        'created_at': datetime.now(UTC).isoformat(),
    }
    return encode(payload, settings.secret_key, algorithm='HS256')


def parse_access_token(token: str) -> UUID | None:
    try:
        payload = decode(token, settings.secret_key, algorithms=['HS256'])
    except InvalidTokenError:
        return

    try:
        data = TokenPayloadSchema(**payload)
    except ValidationError:
        return

    if datetime.now(UTC) < data.created_at + ACCESS_TOKEN_TTL:
        return data.user_id


async def get_user_by_credentials(username: str, password: str) -> User | None:
    user = await User.get_or_none(username=username)

    if user and password_matches(password, user.password):
        return user
