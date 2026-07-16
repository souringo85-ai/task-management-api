from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.core.database import get_db
from app.services import user as user_service
from app.core.auth import get_current_user_id
from app.services.auth import require_admin

router = APIRouter()

class UserCreate(BaseModel):
    name: str
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        from_attributes = True


@router.get("/users", response_model=list[UserResponse])
def get_users(db: Session = Depends(get_db), current_user_id: int = Depends(get_current_user_id)):
    return user_service.get_users(db)

@router.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db), current_user_id: int = Depends(get_current_user_id)):
    user = user_service.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="ユーザーが見つかりません")
    return user

@router.post("/users", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    try:
        return user_service.create_user(db, user.name, user.email, user.password)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.delete("/users/{user_id}", response_model=UserResponse)
def delete_user(user_id: int, org_id: int, db: Session = Depends(get_db), current_user_id: int = Depends(get_current_user_id)):
    require_admin(db, current_user_id, org_id)
    return user_service.delete_user(db, user_id)