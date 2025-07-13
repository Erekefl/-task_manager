from app.models.task import Task
from app.schemas.task import TaskCreate
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List, Optional

async def create_task(db: AsyncSession, task: TaskCreate, user_id: int) -> Task:
    db_task = Task(
        title=task.title,
        description=task.description,
        deadline=task.deadline,
        priority=task.priority,
        user_id=user_id
    )
    db.add(db_task)
    await db.commit()
    await db.refresh(db_task)
    return db_task

async def get_task_by_id(db: AsyncSession, task_id: int) -> Optional[Task]:
    result = await db.execute(select(Task).where(Task.id == task_id))
    return result.scalars().first()

async def get_tasks(db: AsyncSession, user_id: Optional[int] = None) -> List[Task]:
    query = select(Task)
    if user_id is not None:
        query = query.where(Task.user_id == user_id)
    result = await db.execute(query)
    return result.scalars().all()

async def update_task(db: AsyncSession, task_id: int, task_update: TaskCreate) -> Optional[Task]:
    result = await db.execute(select(Task).where(Task.id == task_id))
    db_task = result.scalars().first()
    if not db_task:
        return None
    db_task.title = task_update.title
    db_task.description = task_update.description
    db_task.deadline = task_update.deadline
    db_task.priority = task_update.priority
    await db.commit()
    await db.refresh(db_task)
    return db_task

async def delete_task(db: AsyncSession, task_id: int) -> Optional[Task]:
    result = await db.execute(select(Task).where(Task.id == task_id))
    db_task = result.scalars().first()
    if not db_task:
        return None
    await db.delete(db_task)
    await db.commit()
    return db_task 