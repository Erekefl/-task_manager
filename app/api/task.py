from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.task import TaskCreate, TaskReade
from app.services.task_service import create_task, get_task_by_id, get_tasks, update_task, delete_task
from app.core.database import async_session
from typing import List

router = APIRouter()

async def get_db():
    async with async_session() as session:
        yield session

@router.post("/tasks", response_model=TaskReade)
async def create_task_route(task: TaskCreate, user_id: int, db: AsyncSession = Depends(get_db)):
    db_task = await create_task(db, task, user_id)
    return db_task

@router.get("/tasks", response_model=List[TaskReade])
async def get_tasks_route(user_id: int = None, db: AsyncSession = Depends(get_db)):
    tasks = await get_tasks(db, user_id)
    return tasks

@router.get("/tasks/{task_id}", response_model=TaskReade)
async def get_task_by_id_route(task_id: int, db: AsyncSession = Depends(get_db)):
    db_task = await get_task_by_id(db, task_id)
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task

@router.put("/tasks/{task_id}", response_model=TaskReade)
async def update_task_route(task_id: int, task: TaskCreate, db: AsyncSession = Depends(get_db)):
    db_task = await update_task(db, task_id, task)
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task

@router.delete("/tasks/{task_id}", response_model=TaskReade)
async def delete_task_route(task_id: int, db: AsyncSession = Depends(get_db)):
    db_task = await delete_task(db, task_id)
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task


