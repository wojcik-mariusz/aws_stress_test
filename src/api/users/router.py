from fastapi import APIRouter

router: APIRouter = APIRouter()


@router.get("/r", status_code=200)
def home():
    return {"message": "user_router ok"}
