from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        UPDATE "tasks" SET completed_at = updated_at WHERE status = 'completed';
    """


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        UPDATE "tasks" SET completed_at=null;
    """
