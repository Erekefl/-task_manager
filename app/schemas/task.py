from pydantic import BaseModel
from  typing import Optional
from datetime import datetime


class TaskCreate(BaseModel):
    title : str
    description : Optional[str] = None
    deadline : Optional[datetime] = None
    priority : Optional[int] = 1


class TaskReade(BaseModel):
    id : int
    title : str
    description : Optional[str] = None
    deadline : Optional[datetime] = None
    priority : int
    status : str

    class Config:
        orm_mode = True
