from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .user import Base


class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer,primary_key=True,index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    deadline = Column(DateTime(timezone=True))
    priority = Column(Integer, default=1)
    status = Column(String, default="pending")
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="tasks")

