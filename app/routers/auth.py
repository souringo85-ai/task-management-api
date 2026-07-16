from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.auth import create_access_token
from app.services.user import verify_password
from app.repositories.user import get_user_by_email

router = APIRouter()

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = get_user_by_email(db, form_data.username)
    if not user:
        raise HTTPException(status_code=401, detail="メールアドレスまたはパスワードが間違っています")
    if not verify_password(form_data.password, user.password):
        raise HTTPException(status_code=401, detail="メールアドレスまたはパスワードが間違っています")
    token = create_access_token(data={"sub": str(user.id)})
    return {"access_token": token, "token_type": "bearer"}