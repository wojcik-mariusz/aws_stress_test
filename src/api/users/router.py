from fastapi import APIRouter

router: APIRouter = APIRouter()


@router.get("/r", status_code=200)
def router_root() -> dict[str:str]:
    return {"message": "user_router ok"}
