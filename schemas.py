from pydantic import EmailStr, BaseModel

class UserCreate(BaseModel):
    email : EmailStr
    password : str

class ShowUser(BaseModel):
    email: EmailStr
    is_active: bool

    class Config:
        orm_mode =True