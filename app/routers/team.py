from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.core.database import get_db
from app.services import team as team_service
from app.core.auth import get_current_user_id
from app.services.auth import require_admin

router = APIRouter()

class TeamCreate(BaseModel):
    name: str
    org_id: int

class TeamResponse(BaseModel):
    id: int
    name: str
    org_id: int

    class Config:
        from_attributes = True


@router.get("/teams", response_model=list[TeamResponse])
def get_teams(org_id: int, db: Session = Depends(get_db), current_user_id: int = Depends(get_current_user_id)):
    return team_service.get_teams(db, org_id)

@router.get("/teams/{team_id}", response_model=TeamResponse)
def get_team(team_id: int, org_id: int, db: Session = Depends(get_db), current_user_id: int = Depends(get_current_user_id)):
    team = team_service.get_team(db, team_id, org_id)
    if not team:
        raise HTTPException(status_code=404, detail="チームが見つかりません")
    return team

@router.post("/teams", response_model=TeamResponse)
def create_team(team: TeamCreate, db: Session = Depends(get_db), current_user_id: int = Depends(get_current_user_id)):
    try:
        return team_service.create_team(db, team.name, team.org_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.delete("/teams/{team_id}", response_model=TeamResponse)
def delete_team(org_id: int, team_id: int, db: Session = Depends(get_db), current_user_id: int = Depends(get_current_user_id)):
    require_admin(db, current_user_id, org_id)
    return team_service.delete_team(db, team_id)