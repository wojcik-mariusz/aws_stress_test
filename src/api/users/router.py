from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from src.api.users.security import oauth2_scheme, get_current_user, fake_hash_password
from src.api.users.security import User
from src.api.users.user_db import fake_users_db
from src.api.users.user_schema import UserInDB

router: APIRouter = APIRouter(prefix="/users")


@router.get("/all", status_code=200)
def get_users_list(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"message": "get_all_users", "token": token}


@router.get("/me", status_code=200)
def read_user_me(current_user: Annotated[User, Depends(get_current_user)]):
    return current_user


@router.post("/token")
def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user_dict = fake_users_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect username or password",
        )
    user = UserInDB(**user_dict)
    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect username or password",
        )
    return {"access_token": user.username, "token_type": "bearer"}
