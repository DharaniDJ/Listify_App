from fastapi import APIRouter

router = APIRouter()

@router.get('/items',tags=['products'])
def get_items():
    return {"message":"hello items"}