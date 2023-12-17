from typing import Union, Annotated
from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm

from pydantic import BaseModel


class User(BaseModel):
    username: str
    email: Union[str, None] = None
    full_name: Union[str, None] = None
    disabled: Union[bool, None] = None


class UserInDB(User):
    hashed_password: str
