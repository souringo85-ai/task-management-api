from sqlalchemy.orm import Session
from app.models.task import Task

def get_task(db: Session, task_id: int, team_id: int):
    return db.query(Task).filter(Task.id == task_id, Task.team_id == team_id).first()

def get_task_by_assignee(db: Session, assignee_id: int, team_id: int):
    return db.query(Task).filter(Task.assignee_id == assignee_id, Task.team_id == team_id).all()

def get_tasks(db: Session, team_id: int):
    return db.query(Task).filter(Task.team_id == team_id).all()

def create_task(db: Session, title: str, description: str, status: str, team_id: int, assignee_id: int = None, due_date=None):
    db_task = Task(title=title, description=description, status=status, team_id=team_id, assignee_id=assignee_id, due_date=due_date)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def delete_task(db: Session, task_id: int):
    db_task = db.query(Task).filter(Task.id == task_id).first()
    db.delete(db_task)
    db.commit()
    return db_task