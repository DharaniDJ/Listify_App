from fastapi import APIRouter, Request, Depends, responses, status
from fastapi.templating import Jinja2Templates
from models import Items, User
from sqlalchemy.orm import Session
from database import get_db
from jose import jwt
from config import setting
from datetime import datetime as dt
router = APIRouter(include_in_schema=False)
templates = Jinja2Templates(directory="templates")

@router.get("/")
def item_home(request:Request, db:Session=Depends(get_db), msg:str=None):
    items = db.query(Items).all()
    return templates.TemplateResponse("item_homepage.html",{"request":request, "items":items, "msg":msg})

@router.get("/detail/{id}")
def item_detail(request:Request, id:int, db:Session=Depends(get_db)):
    item = db.query(Items).filter(Items.id==id).first()
    user = db.query(User).filter(User.id==item.owner_id).first()
    return templates.TemplateResponse("item_detail.html",{"request":request, "item":item, "user":user })

@router.get("/create-an-item")
def create_an_item(request:Request):
    return templates.TemplateResponse("create_item.html",{"request":request,})

@router.post("/create-an-item")
async def create_an_item(request:Request, db:Session=Depends(get_db)):
    form = await request.form()
    title = form.get("title")
    description = form.get("description")
    errors = []
    if not title or len(title) < 4:
        errors.append("Title should be > 4 chars")
    if not description or len(description) < 10:
        errors.append("Description should be > 10 chars")
    if len(errors)>0:
        return templates.TemplateResponse("create_item.html",{"request":request, "errors":errors})

    try:
        token = request.cookies.get("access_token")
        if token is None:
            errors.append("Kindly Login first")
            return templates.TemplateResponse("create_item.html",{"request":request, "errors":errors})
        else:
            scheme,_,param = token.partition(" ")
            payload = jwt.decode(param, setting.SECRET_KEY, algorithms=setting.ALGORITHM)
            email = payload.get("sub")
            user = db.query(User).filter_by(email=email).first()
            if user is None:
                errors.append("Your are not Authenticated. Kindly create account or login first")
                return templates.TemplateResponse("create_item.html",{"request":request, "errors":errors})
            else:
                item = Items(title=title, description=description, date_posted=dt.now(),owner_id=user.id)
                db.add(item)
                db.commit()
                db.refresh(item)
                return responses.RedirectResponse(f"/detail/{item.id}",status_code=status.HTTP_302_FOUND)
    except Exception as e:
        errors.append("something is wrong, kindly contact us")
        return templates.TemplateResponse("create_item.html",{"request":request,"errors":errors})

@router.get("/delete-item")
def show_items_to_delete(request:Request, db:Session=Depends(get_db)):
    token = request.cookies.get("access_token")
    errors = []
    if token is None:
        errors.append("You are not logged-in/Authenticated")
        return templates.TemplateResponse("show_items_to_delete.html",{"request":request,"errors":errors})
    else:
        try:
            scheme,_,param = token.partition(" ")
            payload = jwt.decode(param, setting.SECRET_KEY,algorithms=setting.ALGORITHM)
            email = payload.get("sub")
            user = db.query(User).filter(User.email==email).first()
            items = db.query(Items).filter(Items.owner_id==user.id).all()
            return templates.TemplateResponse("show_items_to_delete.html",{"request":request,"items":items})
        except Exception as e:
            errors.append("Something is wrong")
            print(e)
            return templates.TemplateResponse("show_items_to_delete.html",{"request":request,"errors":errors})