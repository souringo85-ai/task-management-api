from sqlalchemy.orm import Session
from app.repositories import team as team_repo

def create_team(db: Session, name: str, org_id: int):
    existing_team = team_repo.get_team_by_name_orgid(db, name, org_id)
    if existing_team:
        raise ValueError("このチームは既に登録されています")
    return team_repo.create_team(db, name, org_id)

def delete_team(db: Session, team_id: int):
    return team_repo.delete_team(db, team_id)

def get_team(db: Session, team_id: int, org_id: int):
    return team_repo.get_team(db, team_id, org_id)

def get_team_by_name_orgid(db: Session, name:str, org_id: int):
    return team_repo.get_team_by_name_orgid(db, name, org_id)

def get_teams(db: Session, org_id: int):
    return team_repo.get_teams(db, org_id)