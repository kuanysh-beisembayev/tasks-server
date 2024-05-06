from uuid import UUID

from fastapi import Response, status
from fastapi.responses import JSONResponse
from tortoise.exceptions import IntegrityError

from code.models import Task
from code.schemas import TaskCreateSchema, TaskUpdateSchema
from code.utils import serialize_task


async def task_list_handler() -> Response:
    tasks = await Task.all().order_by('-updated_at', '-created_at')
    return JSONResponse([
        serialize_task(task) for task in tasks
    ])


async def task_detail_handler(task_id: UUID) -> Response:
    task = await Task.get_or_none(id=task_id)

    if task is None:
        return Response(status_code=status.HTTP_404_NOT_FOUND)

    return JSONResponse(serialize_task(task))


async def task_create_handler(data: TaskCreateSchema) -> Response:
    try:
        task = await Task.create(
            name=data.name,
            status=Task.Status.NEW,
        )
    except IntegrityError:
        return Response(status_code=status.HTTP_400_BAD_REQUEST)

    return JSONResponse(serialize_task(task))


async def task_update_handler(task_id: UUID, data: TaskUpdateSchema) -> Response:
    task = await Task.get_or_none(id=task_id)

    if task is None:
        return Response(status_code=status.HTTP_404_NOT_FOUND)

    task.name = data.name
    task.description = data.description
    task.status = data.status
    await task.save()
    return JSONResponse(serialize_task(task))
