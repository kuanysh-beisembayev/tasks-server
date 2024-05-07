from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "tasks" DROP COLUMN "priority";
        ALTER TABLE "tasks" ALTER COLUMN "status" TYPE VARCHAR(9) USING "status"::VARCHAR(9);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "tasks" ADD "priority" INT NOT NULL  DEFAULT 0;
        ALTER TABLE "tasks" ALTER COLUMN "status" TYPE VARCHAR(11) USING "status"::VARCHAR(11);"""
