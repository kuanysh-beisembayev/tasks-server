from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "tasks" (
    "id" UUID NOT NULL  PRIMARY KEY,
    "name" VARCHAR(100) NOT NULL,
    "description" VARCHAR(100),
    "priority" INT NOT NULL  DEFAULT 0,
    "status" VARCHAR(11) NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP
);
COMMENT ON COLUMN "tasks"."status" IS 'NEW: new\nIN_PROGRESS: in_progress\nDONE: done';
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
