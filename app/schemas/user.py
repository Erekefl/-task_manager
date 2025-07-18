from typing import Optional

from pydantic import BaseModel,EmailStr,constr

class UserCreate(BaseModel):
      username: constr(min_length=3, max_length=20)
      email : EmailStr
      password : constr(min_length=3)
      city: Optional[str] = None

class UserRead(BaseModel):
    id : int
    username : str
    email : EmailStr
    city: Optional[str] = None

    class Config:
        orm_mode = True

