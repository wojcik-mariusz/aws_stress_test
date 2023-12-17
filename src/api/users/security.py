from typing import Annotated
from jose import jwt, JWTError
from passlib.context import CryptContext
from pydantic import BaseModel
from dotenv import load_dotenv
from os import environ

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from src.api.users.user_db import fake_users_db

from src.api.users.user_schema import User, UserInDB

load_dotenv(".env")

SECRET_KEY: str = environ.get("SECRET_KEY")
ALGORITHM: str = environ.get("ALGORITHM")


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme: OAuth2PasswordBearer = OAuth2PasswordBearer(tokenUrl="users/token")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str):
    return pwd_context.hash(password)


def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)


def fake_decode_token(token: str) -> User:
    user = get_user(fake_users_db, token)
    return user


def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user


def get_current_active_user(current_user: Annotated[User, Depends(get_current_user)]):
    if current_user.disabled:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Inactive user"
        )
    return current_user
