from fastapi import FastAPI

from src.api.users.router import router as user_router

app: FastAPI = FastAPI()


@app.get("/", status_code=200)
def read_root():
    return {"message": "server running"}


app.include_router(router=user_router, tags=["users"])
