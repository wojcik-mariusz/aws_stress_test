from fastapi import FastAPI

from src.api.users import router as users_router

app: FastAPI = FastAPI()


@app.get("/", status_code=200)
def read_root() -> dict[str: str]:
    return {"message": "server running"}


app.include_router(router=users_router.router)
