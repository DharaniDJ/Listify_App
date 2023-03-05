from pydantic import EmailStr, BaseModel

class UserCreate(BaseModel):
    email : EmailStr
    password : str

class ShowUser(BaseModel):
    email: EmailStr
    is_active: bool

    class Config:
        orm_mode =True  # return dictionary, by default it returns an object