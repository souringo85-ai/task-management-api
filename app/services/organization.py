from sqlalchemy.orm import Session
from app.repositories import organization as org_repo

def create_org(db: Session, name: str):
    existing_org = org_repo.get_organization_by_name(db, name)
    if existing_org:
        raise ValueError("この組織名は既に登録されています")
    return org_repo.create_organization(db, name)

def delete_org(db: Session, org_id: int):
    return org_repo.delete_organization(db, org_id)

def get_org(db: Session, org_id: int):
    return org_repo.get_organization(db, org_id)

def get_org_by_name(db: Session, org_name: str):
    return org_repo.get_organization_by_name(db, org_name)

def get_orgs(db:Session):
    return org_repo.get_organizations(db)