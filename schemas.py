from pydantic import EmailStr, BaseModel

class UserCreate(BaseModel):
    email : EmailStr
    password : str