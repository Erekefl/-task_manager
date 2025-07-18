from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, relationship
from app.core.config import DATABASE_URL

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key=True,index = True)
    username = Column(String,unique=True,index=True,nullable=False)
    email=Column(String,unique=True,index=True,nullable=False)
    hashed_password = Column(String, nullable=False)
    city = Column(String, nullable=True)


    tasks = relationship("Task", back_populates="user")

from .task import Task
