from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "tasks" DROP COLUMN "deadline_at";
        ALTER TABLE "tasks" DROP COLUMN "description";"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "tasks" ADD "deadline_at" DATE;
        ALTER TABLE "tasks" ADD "description" VARCHAR(100);"""
