from uuid import UUID

from fastapi import Depends, Response, status
from fastapi.responses import JSONResponse
from tortoise.exceptions import IntegrityError

from src.dependencies import get_user
from src.models import Task, User
from src.schemas import AuthSchema, TaskCreateSchema, TaskUpdateSchema
from src.utils import create_access_token, get_user_by_credentials, serialize_task


async def tokens_handler(data: AuthSchema) -> Response:
    user = await get_user_by_credentials(data.username, data.password)

    if user is None:
        return Response(status_code=status.HTTP_400_BAD_REQUEST)

    return JSONResponse({'access_token': create_access_token(user.id)})


async def task_list_handler(user: User = Depends(get_user)) -> Response:
    tasks = await Task.filter(user=user).order_by('-updated_at', '-created_at')
    return JSONResponse([
        serialize_task(task) for task in tasks
    ])


async def task_detail_handler(task_id: UUID, user: User = Depends(get_user)) -> Response:
    task = await Task.get_or_none(id=task_id, user=user)

    if task is None:
        return Response(status_code=status.HTTP_404_NOT_FOUND)

    return JSONResponse(serialize_task(task))


async def task_create_handler(data: TaskCreateSchema, user: User = Depends(get_user)) -> Response:
    try:
        task = await Task.create(
            name=data.name,
            status=data.status,
            user=user,
        )
    except IntegrityError:
        return Response(status_code=status.HTTP_400_BAD_REQUEST)

    return JSONResponse(serialize_task(task))


async def task_update_handler(
    task_id: UUID, data: TaskUpdateSchema, user: User = Depends(get_user),
) -> Response:
    task = await Task.get_or_none(id=task_id, user=user)

    if task is None:
        return Response(status_code=status.HTTP_404_NOT_FOUND)

    task.name = data.name
    task.status = data.status
    await task.save()
    return JSONResponse(serialize_task(task))
