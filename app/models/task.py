from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from app.core.database import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    due_date = Column(DateTime)
    status = Column(String, nullable=False)
    assignee_id = Column(Integer, ForeignKey("users.id"))
    team_id = Column(Integer, ForeignKey("teams.id"))