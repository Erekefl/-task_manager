import asyncio
from app.models.user import Base
from app.models import task
from app.core.database import engine

async def create_all_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

if __name__ == "__main__":
    asyncio.run(create_all_tables())