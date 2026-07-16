from sqlalchemy.orm import Session
from app.models.team import Team

def get_team(db: Session, team_id: int, org_id: int):
    return db.query(Team).filter(Team.id == team_id, Team.org_id == org_id).first()

def get_team_by_name_orgid(db: Session, name:str, org_id: int):
    return db.query(Team).filter(Team.name == name, Team.org_id == org_id).first()

def get_teams(db: Session, org_id: int):
    return db.query(Team).filter(Team.org_id == org_id).all()

def create_team(db: Session, name: str, org_id: int):
    db_team = Team(name=name, org_id=org_id)
    db.add(db_team)
    db.commit()
    db.refresh(db_team)
    return db_team

def delete_team(db: Session, team_id: int):
    db_team = db.query(Team).filter(Team.id == team_id).first()
    db.delete(db_team)
    db.commit()
    return db_team