from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.user import UserCreate, UserRead
from app.services.user_service import create_user, get_user_by_email, get_user_name, update_user, delete_user,get_user_id
from app.core.database import async_session


router = APIRouter()

async def get_db():
    async with async_session() as session:
        yield session

@router.post("/register", response_model=UserRead)
async def register(user: UserCreate, db: AsyncSession = Depends(get_db)):
    db_user = await get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return await create_user(db, user)

@router.get("/by_email", response_model=UserRead)
async def get_by_email(email: str, db: AsyncSession = Depends(get_db)):
    db_user = await get_user_by_email(db, email)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.get("/by_username",response_model=UserRead)
async def get_user_by_name(username: str,db:AsyncSession = Depends(get_db)):
    db_user = await get_user_name(db,username)
    if not db_user:
        raise HTTPException(status_code=404,detail="User not found")
    return db_user



@router.get("/{user_id}", response_model=UserRead)
async def get_user_by_id(user_id: int, db: AsyncSession = Depends(get_db)):
    db_user = await get_user_id(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.put("/{user_id}", response_model=UserRead)
async def update_user_route(user_id: int, user: UserCreate, db: AsyncSession = Depends(get_db)):
    db_user = await update_user(db, user_id, user)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.delete("/{user_id}", response_model=UserRead)
async def delete_user_route(user_id: int, db: AsyncSession = Depends(get_db)):
    db_user = await delete_user(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user



