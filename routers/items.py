from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from schemas import ItemCreate, ShowItem
from models import Items
from datetime import datetime
from sqlalchemy.orm import Session
from database import get_db
from fastapi.encoders import jsonable_encoder

router = APIRouter()

@router.post('/item',tags=["items"],response_model=ShowItem)
def create_items(item:ItemCreate,db:Session=Depends(get_db)):
    date_posted = datetime.now().date()
    owner_id=1
    item = Items(**item.dict(),date_posted=date_posted,owner_id=owner_id)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

@router.get("/item/all",tags=["items"], response_model=List[ShowItem])
def retrieve_all_items(db:Session=Depends(get_db)):
    items = db.query(Items).all()
    return items

@router.get("/item/{id}",tags=["items"], response_model=ShowItem)
def retrieve_item_by_id(id:int, db:Session=Depends(get_db)):
    item = db.query(Items).filter(Items.id==id).first()
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Item {id} does not exists")
    return item

@router.put("/item/update/{id}",tags=["items"])
def update_item_by_id(id:int, item:ItemCreate,db:Session=Depends(get_db)):
    existing_item = db.query(Items).filter(Items.id==id)
    if not existing_item.first():
        return {"message":f'No details exists for Item ID {id}'}

    existing_item.update(jsonable_encoder(item)) # update keyword require jsonable_encoder, we can use item.__dict__ also
    db.commit()
    return {"message":f"Details for Item ID {id} successfully updated"}
