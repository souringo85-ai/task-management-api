from sqlalchemy.orm import Session
from app.repositories import task as task_repo

def create_task(db: Session, title: str, description: str, status: str, team_id: int, assignee_id: int = None, due_date=None):
    return task_repo.create_task(db, title, description, status, team_id, assignee_id, due_date)

def delete_task(db: Session, task_id: int):
    return task_repo.delete_task(db, task_id)

def get_task(db: Session, task_id: int, team_id: int):
    return task_repo.get_task(db, task_id, team_id)

def get_task_by_assignee(db: Session, assignee_id: int, team_id: int):
    return task_repo.get_task_by_assignee(db, assignee_id, team_id)

def get_tasks(db: Session, team_id: int):
    return task_repo.get_tasks(db, team_id)