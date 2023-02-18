from fastapi import FastAPI
from config import setting

tags_metadata = [
    {
        "name":"user",
        "description":"This is user route"
    },
    {
        "name":"products",
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


@app.get('/users',tags=["user"])
def get_user():
    return {"message":"hello user"}



@app.get('/items',tags=['products'])
def get_items():
    return {"message":"hello items"}

@app.get('/getenv',tags=["config"])
def get_env():
    return {"database":setting.DB_URL}