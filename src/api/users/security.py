from typing import Annotated
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from src.api.users.user_db import fake_users_db

from src.api.users.user_schema import User, UserInDB

oauth2_scheme: OAuth2PasswordBearer = OAuth2PasswordBearer(tokenUrl="token")


def get_user(db, username:str):
        if username in db:
            user_dict = db[username]
            return UserInDB(**user_dict)


def fake_decode_token(token: str) -> User:
    pass



def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]) -> User:
    user = fake_decode_token(token)
    return user


def fake_hash_password(password: str) -> str:
    return "fakehashed" + password
