from fastapi import FastAPI
from config import setting
from database import engine
from models import Base
from routers import users, items, login
from webapps.routers import items as web_items
from webapps.routers import users as web_users
from fastapi.staticfiles import StaticFiles


# we are using alembic migrations
# Base.metadata.create_all(bind=engine)

tags_metadata = [
    {
        "name":"user",
        "description":"This is user route"
    },
    {
        "name":"items",
        "description":"This is product route"
    }
]

app = FastAPI(
    title=setting.TITLE,
    version=setting.VERSION,
    description=setting.DESCRIPTION,
    openapi_tags=tags_metadata,
    contact={"name":setting.NAME,"email":setting.EMAIL}
)

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(users.router)
app.include_router(items.router)
app.include_router(login.router)
app.include_router(web_items.router)
app.include_router(web_users.router)