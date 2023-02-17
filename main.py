from fastapi import FastAPI

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
    title="My FastAPI",
    version="0.0.01",
    description="This is test project",
    openapi_tags=tags_metadata,
    contact={"name":"Dharani","email":"dharani56525@gmail.com"}
)


@app.get('/users',tags=["user"])
def get_user():
    return {"message":"hello user"}



@app.get('/items',tags=['products'])
def get_items():
    return {"message":"hello items"}

