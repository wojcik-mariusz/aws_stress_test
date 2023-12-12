from typing import Annotated
from fastapi import APIRouter, Depends

from src.api.users.security import oauth2_scheme, get_current_user
from src.api.users.security import User

router: APIRouter = APIRouter(prefix="/users")


@router.get("/all", status_code=200)
def get_users_list(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"message": "get_all_users", "token": token}


@router.get("/me", status_code=200)
def read_user_me(current_user: Annotated[User, Depends(get_current_user)]):
    return current_user
