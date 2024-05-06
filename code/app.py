from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise
from uvicorn import run

from code import handlers
from code.config import settings, TORTOISE_CONFIG

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)
app.add_api_route('/tasks', handlers.task_list_handler)
app.add_api_route('/tasks/{task_id}', handlers.task_detail_handler)
app.add_api_route('/tasks', handlers.task_create_handler, methods=['post'])
app.add_api_route('/tasks/{task_id}', handlers.task_update_handler, methods=['put'])
register_tortoise(app, config=TORTOISE_CONFIG)

if __name__ == '__main__':
    run('code.app:app', host='0.0.0.0', reload=settings.debug, port=settings.port)
