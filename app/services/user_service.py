from passlib.context import CryptContext
from app.models.user import User
from app.schemas.user import UserCreate
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

async def get_user_by_email(db: AsyncSession, email: str):
    result = await db.execute(select(User).where(User.email == email))
    return result.scalars().first()

async def create_user(db: AsyncSession, user: UserCreate):
    hashed_password = pwd_context.hash(user.password)
    db_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password,
        city=user.city
    )
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user



async def update_user(db: AsyncSession, user_id: int, user_update: UserCreate):
    result = await db.execute(select(User).where(User.id == user_id))
    db_user = result.scalars().first()
    if not db_user:
        return None
    db_user.username = user_update.username
    db_user.email = user_update.email
    db_user.hashed_password = pwd_context.hash(user_update.password)
    db_user.city=user_update.city
    await db.commit()
    await db.refresh(db_user)
    return db_user

async def delete_user(db: AsyncSession, user_id: int):
    from sqlalchemy.future import select
    result = await db.execute(select(User).where(User.id == user_id))
    db_user = result.scalars().first()
    if not db_user:
        return None
    await db.delete(db_user)
    await db.commit()
    return db_user

async def get_user_name(db:AsyncSession,username:str):
    result = await db.execute(select(User).where(User.username == username))
    return result.scalars().first()

async def get_user_id(db:AsyncSession,user_id:int):
    result = await db.execute(select(User).where(User.id == user_id))
    return result.scalars().first()





