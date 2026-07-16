from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.core.database import get_db
from app.services import organization as org_service
from app.core.auth import get_current_user_id
from app.services.auth import require_admin

router = APIRouter()

class OrgCreate(BaseModel):
    name: str

class OrgResponse(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True


@router.get("/orgs", response_model=list[OrgResponse])
def get_orgs(db: Session = Depends(get_db), current_user_id: int = Depends(get_current_user_id)):
    return org_service.get_orgs(db)

@router.get("/orgs/{org_id}", response_model=OrgResponse)
def get_org(org_id: int, db: Session = Depends(get_db), current_user_id: int = Depends(get_current_user_id)):
    org = org_service.get_org(db, org_id)
    if not org:
        raise HTTPException(status_code=404, detail="組織が見つかりません")
    return org

@router.post("/orgs", response_model=OrgResponse)
def create_org(org: OrgCreate, db: Session = Depends(get_db), current_user_id: int = Depends(get_current_user_id)):
    try:
        return org_service.create_org(db, org.name)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.delete("/orgs/{org_id}")
def delete_org(org_id: int, db: Session = Depends(get_db), current_user_id: int = Depends(get_current_user_id)):
    require_admin(db, current_user_id, org_id)
    org = org_service.delete_org(db, org_id)
    if not org:
        raise HTTPException(status_code=404, detail="組織が見つかりません")
    return org