from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.core.database import get_db
from app.services import team_member as team_member_service
from app.core.auth import get_current_user_id

router = APIRouter()

class TeamMemberCreate(BaseModel):
    user_id: int
    team_id: int

class TeamMemberResponse(BaseModel):
    id: int
    user_id: int
    team_id: int

    class Config:
        from_attributes = True


@router.get("/team_members", response_model=list[TeamMemberResponse])
def get_team_members(team_id: int, db: Session = Depends(get_db), current_user_id: int = Depends(get_current_user_id)):
    return team_member_service.get_team_members(db, team_id)

@router.get("/team_member", response_model=TeamMemberResponse)
def get_team_member(user_id: int, team_id: int, db: Session = Depends(get_db), current_user_id: int = Depends(get_current_user_id)):
    team_member = team_member_service.get_team_member(db, user_id, team_id)
    if not team_member:
        raise HTTPException(status_code=404, detail="メンバーが見つかりません")
    return team_member

@router.post("/team_members", response_model=TeamMemberResponse)
def create_team_member(team_member: TeamMemberCreate, db: Session = Depends(get_db), current_user_id: int = Depends(get_current_user_id)):
    try:
        return team_member_service.create_team_member(db, team_member.user_id, team_member.team_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.delete("/team_members", response_model=TeamMemberResponse)
def delete_team_member(user_id: int, team_id: int, db: Session = Depends(get_db), current_user_id: int = Depends(get_current_user_id)):
    return team_member_service.delete_team_member(db, user_id, team_id)