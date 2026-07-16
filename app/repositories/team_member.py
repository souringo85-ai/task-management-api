from sqlalchemy.orm import Session
from app.models.team_member import TeamMember

def get_team_member(db: Session, user_id: int, team_id: int):
    return db.query(TeamMember).filter(TeamMember.user_id == user_id, TeamMember.team_id == team_id).first()

def get_team_members(db: Session, team_id: int):
    return db.query(TeamMember).filter(TeamMember.team_id == team_id).all()

def create_team_member(db: Session, user_id: int, team_id: int):
    db_team_member = TeamMember(user_id=user_id, team_id=team_id)
    db.add(db_team_member)
    db.commit()
    db.refresh(db_team_member)
    return db_team_member

def delete_team_member(db: Session, user_id: int, team_id: int):
    db_team_member = db.query(TeamMember).filter(TeamMember.user_id == user_id, TeamMember.team_id == team_id).first()
    db.delete(db_team_member)
    db.commit()
    return db_team_member