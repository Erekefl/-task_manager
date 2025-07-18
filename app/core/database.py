from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from app.core.config import DATABASE_URL

engine = create_async_engine(DATABASE_URL,echo=True)
async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
