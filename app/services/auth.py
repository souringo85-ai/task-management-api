from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.repositories.org_member import get_org_member

def require_admin(db: Session, user_id: int, org_id: int):
    org_member = get_org_member(db, user_id, org_id)
    if not org_member:
        raise HTTPException(status_code=403, detail="この組織のメンバーではありません")
    if org_member.role != "admin":
        raise HTTPException(status_code=403, detail="管理者権限が必要です")