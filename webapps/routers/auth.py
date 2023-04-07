from fastapi import APIRouter, Request, Depends, Response
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from models import User
from database import get_db
from hashing import Hasher
from jose import jwt
from config import setting

router = APIRouter(include_in_schema=False)
templates = Jinja2Templates(directory="templates")

@router.get("/login")
def login(request:Request, msg:str=None):
    return templates.TemplateResponse("login.html",{"request":request, "msg":msg})

# use async method while using forms
@router.post("/login")
async def login(response:Response, request:Request, db:Session=Depends(get_db)):
    form = await request.form()
    email = form.get("email")
    password = form.get("password")
    errors=[]
    if not email:
        errors.append("Please enter valid email")
    if not password or len(password)<5:
        errors.append("Password should be > 5 characters")
    try:
        user = db.query(User).filter(User.email==email).first()
        if user is None:
            errors.append("Email does not exist")
            return templates.TemplateResponse("login.html",{"request":request ,"errors":errors})

        if Hasher.verify_password(password, user.password):
            data = {"sub":email}
            jwt_token = jwt.encode(data,setting.SECRET_KEY, algorithm=setting.ALGORITHM)
            msg = "Login Successful"
            response = templates.TemplateResponse("login.html",{"request":request, "msg":msg})
            response.set_cookie(key="access_token", value=f"Bearer {jwt_token}", httponly=True)
            return response
        else:
            errors.append("Invalid password")
            return templates.TemplateResponse("login.html",{"request":request,"errors":errors})
    except Exception as e:
        errors.append("Something wrong!!")
        return templates.TemplateResponse("login.html",{"request":request,"errors":errors})