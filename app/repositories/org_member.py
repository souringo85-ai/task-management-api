from sqlalchemy.orm import Session
from app.models.org_member import OrgMember

def get_org_member(db: Session, user_id: int, org_id: int):
    return db.query(OrgMember).filter(OrgMember.user_id == user_id, OrgMember.org_id == org_id).first()

def get_org_member_by_orgid_role(db: Session, org_id: int, role: str):
    return db.query(OrgMember).filter(OrgMember.org_id == org_id, OrgMember.role == role).all()

def get_org_members(db: Session, org_id: int):
    return db.query(OrgMember).filter(OrgMember.org_id == org_id).all()

def create_org_member(db: Session, user_id: int, org_id: int, role: str):
    db_org_member = OrgMember(user_id=user_id, org_id=org_id, role=role)
    db.add(db_org_member)
    db.commit()
    db.refresh(db_org_member)
    return db_org_member

def delete_org_member(db: Session, user_id: int, org_id: int):
    db_org_member = db.query(OrgMember).filter(OrgMember.user_id == user_id, OrgMember.org_id == org_id).first()
    db.delete(db_org_member)
    db.commit()
    return db_org_member