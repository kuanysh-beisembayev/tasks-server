from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise
from uvicorn import run

from src import handlers
from src.config import settings, TORTOISE_CONFIG

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)
app.add_api_route('/auth/tokens', handlers.tokens_handler, methods=['post'])
app.add_api_route('/tasks', handlers.task_list_handler)
app.add_api_route('/tasks/{task_id}', handlers.task_detail_handler)
app.add_api_route('/tasks', handlers.task_create_handler, methods=['post'])
app.add_api_route('/tasks/{task_id}', handlers.task_update_handler, methods=['put'])
app.add_api_route('/tasks/{task_id}/status', handlers.task_status_update_handler, methods=['post'])
register_tortoise(app, config=TORTOISE_CONFIG)

if __name__ == '__main__':
    run('src.app:app', host='0.0.0.0', reload=settings.debug, port=settings.port)
