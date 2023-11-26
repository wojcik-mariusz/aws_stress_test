from fastapi import APIRouter

router: APIRouter = APIRouter(prefix="/users")


@router.get("/all", status_code=200)
def get_users_list():
    return {"message": "get_all_users"}
