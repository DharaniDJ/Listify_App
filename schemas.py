from pydantic import EmailStr, BaseModel

class Users(BaseModel):
    email : EmailStr
    password : str