from sqlalchemy.orm import Session
from app.models.organization import Organization

def get_organization(db: Session, organization_id: int):
    return db.query(Organization).filter(Organization.id == organization_id).first()

def get_organization_by_name(db: Session, name:str):
    return db.query(Organization).filter(Organization.name == name).first()

def get_organizations(db: Session):
    return db.query(Organization).all()

def create_organization(db: Session, name: str):
    db_organization = Organization(name=name)
    db.add(db_organization)
    db.commit()
    db.refresh(db_organization)
    return db_organization

def delete_organization(db: Session, organization_id: int):
    db_organization = db.query(Organization).filter(Organization.id == organization_id).first()
    if not db_organization:
        return None
    db.delete(db_organization)
    db.commit()
    return db_organization

