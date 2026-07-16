from sqlalchemy.orm import Session
from app.repositories import team_member as team_member_repo

def create_team_member(db: Session, user_id: int, team_id: int):
    existings_team_member = team_member_repo.get_team_member(db, user_id, team_id)
    if existings_team_member:
        raise ValueError("このメンバーは既に登録されています")
    return team_member_repo.create_team_member(db, user_id, team_id)

def delete_team_member(db: Session, user_id: int, team_id: int):
    return team_member_repo.delete_team_member(db, user_id, team_id)

def get_team_member(db: Session, user_id: int, team_id: int):
    return team_member_repo.get_team_member(db, user_id, team_id)

def get_team_members(db: Session, team_id: int):
    return team_member_repo.get_team_members(db, team_id)