from sqlalchemy.orm import Session
from app.repositories import user as user_repo
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    passwod = password[:72]
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def get_user(db: Session, user_id: int):
    return user_repo.get_user(db, user_id)

def get_users(db: Session):
    return user_repo.get_users(db)

def create_user(db: Session, name: str, email: str, password: str):
    existing_user = user_repo.get_user_by_email(db, email)
    if existing_user:
        raise ValueError("このメールアドレスは既に登録されています")
    hashed_password = hash_password(password)
    return user_repo.create_user(db, name, email, hashed_password)

def delete_user(db: Session, user_id: int):
    return user_repo.delete_user(db, user_id)