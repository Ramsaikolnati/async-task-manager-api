from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.db import async_session
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate, TaskResponse
from app.api.users import get_current_user
from app.models.user import User

router = APIRouter(prefix="/tasks", tags=["Tasks"])

async def get_db():
    async with async_session() as session:
        yield session

@router.post("/", response_model=TaskResponse, status_code=201)
async def create_task(task: TaskCreate, db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    new_task = Task(title=task.title, description=task.description, owner_id=current_user.id)
    db.add(new_task)
    await db.commit()
    await db.refresh(new_task)
    return new_task

@router.get("/", response_model=list[TaskResponse])
async def list_tasks(db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    result = await db.execute(select(Task).where(Task.owner_id == current_user.id))
    return result.scalars().all()

@router.get("/{task_id}", response_model=TaskResponse)
async def get_task(task_id: int, db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    res = await db.execute(select(Task).where(Task.id == task_id, Task.owner_id == current_user.id))
    task = res.scalar_one_or_none()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.patch("/{task_id}", response_model=TaskResponse)
async def update_task(task_id: int, payload: TaskUpdate, db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    res = await db.execute(select(Task).where(Task.id == task_id, Task.owner_id == current_user.id))
    task = res.scalar_one_or_none()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    if payload.title is not None:
        task.title = payload.title
    if payload.description is not None:
        task.description = payload.description
    if payload.completed is not None:
        task.completed = payload.completed
    await db.commit()
    await db.refresh(task)
    return task

@router.delete("/{task_id}", status_code=204)
async def delete_task(task_id: int, db: AsyncSession = Depends(get_db), current_user: User = Depends(get_current_user)):
    res = await db.execute(select(Task).where(Task.id == task_id, Task.owner_id == current_user.id))
    task = res.scalar_one_or_none()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    await db.delete(task)
    await db.commit()
    return None
