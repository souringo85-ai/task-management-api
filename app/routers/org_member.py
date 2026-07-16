from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.core.database import get_db
from app.services import org_member as org_member_service
from app.core.auth import get_current_user_id
from app.services.auth import require_admin

router = APIRouter()

class OrgMemberCreate(BaseModel):
    user_id: int
    org_id: int
    role: str

class OrgMemberResponse(BaseModel):
    id: int
    user_id: int
    org_id: int
    role: str

    class Config:
        from_attributes = True


@router.get("/org_members", response_model=list[OrgMemberResponse])
def get_org_members(org_id: int, db: Session = Depends(get_db), current_user_id: int = Depends(get_current_user_id)):
    return org_member_service.get_org_members(db, org_id)

@router.get("/org_member", response_model=OrgMemberResponse)
def get_org_member(user_id: int, org_id: int, db: Session = Depends(get_db), current_user_id: int = Depends(get_current_user_id)):
    org_member = org_member_service.get_org_member(db, user_id, org_id)
    if not org_member:
        raise HTTPException(status_code=404, detail="メンバーが見つかりません")
    return org_member

@router.post("/org_members", response_model=OrgMemberResponse)
def create_org_member(org_id: int, org_member: OrgMemberCreate, db: Session = Depends(get_db), current_user_id: int = Depends(get_current_user_id)):
    try:
        require_admin(db, current_user_id, org_id)
        return org_member_service.create_org_member(db, org_member.user_id, org_member.org_id, org_member.role)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.delete("/org_members", response_model=OrgMemberResponse)
def delete_org_member(user_id: int, org_id: int, db: Session = Depends(get_db), current_user_id: int = Depends(get_current_user_id)):
    require_admin(db, current_user_id, org_id)
    return org_member_service.delete_org_member(db, user_id, org_id)