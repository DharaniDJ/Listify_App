
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas import UserCreate
from database import get_db
from hashing import Hasher
from models import User

router = APIRouter()

@router.get('/users',tags=["user"])
def get_user():
    return {"message":"hello user"}

@router.post('/users', tags=["user"])
def create_user(user : UserCreate, db:Session=Depends(get_db)):
    user = User(email=user.email, password=Hasher.get_hash_password(user.password))
    db.add(user)
    db.commit()
    db.refresh(user)
    return user