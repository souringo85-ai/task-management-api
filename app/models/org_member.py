from sqlalchemy import Column, Integer, String, ForeignKey
from app.core.database import Base

class OrgMember(Base):
    __tablename__ = "org_members"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    org_id = Column(Integer, ForeignKey("organizations.id"))
    role = Column(String)