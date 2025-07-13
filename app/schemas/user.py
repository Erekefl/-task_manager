from pydantic import BaseModel,EmailStr,constr

class UserCreate(BaseModel):
      username: constr(min_length=3, max_length=20)
      email : EmailStr
      password : constr(min_length=3)

class UserRead(BaseModel):
    id : int
    username : str
    email : EmailStr

    class Config:
        orm_mode = True

