from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE UNIQUE INDEX "uid_tasks_name_1ac525" ON "tasks" ("name");"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP INDEX "idx_tasks_name_1ac525";"""
