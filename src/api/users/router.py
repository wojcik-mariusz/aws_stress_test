import datetime
import os
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from src.api.users.security import (
    oauth2_scheme,
    get_current_user,
    get_current_active_user,
    authenticate_user,
    create_access_token,
)
from src.api.users.security import User
from src.api.users.user_db import fake_users_db

ACCESS_TOKEN_EXPIRE_MINUTES = os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES")

router: APIRouter = APIRouter(prefix="/users")


@router.get("/all", status_code=200)
def get_users_list(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"message": "get_all_users", "token": token}


@router.get("/me", status_code=200)
def read_user_me(current_user: Annotated[User, Depends(get_current_user)]):
    return current_user


@router.post("/token")
def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect username or password",
        )
    access_token_expires = datetime.timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES))
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("users/me", status_code=200)
def read_user_me(current_user: Annotated[User, Depends(get_current_active_user)]):
    return current_user
