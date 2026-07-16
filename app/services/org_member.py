from sqlalchemy.orm import Session
from app.repositories import org_member as org_member_repo

def create_org_member(db: Session, user_id: int, org_id: int, role: str):
    existings_org_member = org_member_repo.get_org_member(db, user_id, org_id)
    if existings_org_member:
        raise ValueError("このメンバーは既に登録されています")
    return org_member_repo.create_org_member(db, user_id, org_id, role)

def delete_org_member(db: Session, user_id: int, org_id: int):
    return org_member_repo.delete_org_member(db, user_id, org_id)

def get_org_member(db: Session, user_id: int, org_id: int):
    return org_member_repo.get_org_member(db, user_id, org_id)

def get_org_member_by_orgid_role(db: Session, org_id: int, role: str):
    return org_member_repo.get_org_member_by_orgid_role(db, org_id, role)

def get_org_members(db: Session, org_id: int):
    return org_member_repo.get_org_members(db, org_id)