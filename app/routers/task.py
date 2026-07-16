from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.core.database import get_db
from app.services import task as task_service
from datetime import datetime
from app.core.auth import get_current_user_id

router = APIRouter()

class TaskCreate(BaseModel):
    title: str
    description: str
    due_date: datetime = None
    status: str
    assignee_id: int = None
    team_id: int

class TaskResponse(BaseModel):
    id: int
    title: str
    description: str
    due_date: datetime = None
    status: str
    assignee_id: int = None
    team_id: int

    class Config:
        from_attributes = True


@router.get("/tasks", response_model=list[TaskResponse])
def get_tasks(team_id: int, db: Session = Depends(get_db), current_user_id: int = Depends(get_current_user_id)):
    return task_service.get_tasks(db, team_id)

@router.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task(task_id: int, team_id: int, db: Session = Depends(get_db), current_user_id: int = Depends(get_current_user_id)):
    task = task_service.get_task(db, task_id, team_id)
    if not task:
        raise HTTPException(status_code=404, detail="タスクが見つかりません")
    return task

@router.post("/tasks", response_model=TaskResponse)
def create_task(task: TaskCreate, db: Session = Depends(get_db), current_user_id: int = Depends(get_current_user_id)):
    try:
        return task_service.create_task(db, task.title, task.description, task.status, task.team_id, task.assignee_id, task.due_date)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.delete("/tasks/{task_id}", response_model=TaskResponse)
def delete_task(task_id: int, db: Session = Depends(get_db), current_user_id: int = Depends(get_current_user_id)):
    return task_service.delete_task(db, task_id)