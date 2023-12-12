from typing import Union, Annotated
from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm

from pydantic import BaseModel

from src.api.users.security import oauth2_scheme


class User(BaseModel):
    username: str
    email: Union[str, None] = None
    full_name: Union[str, None] = None
    disabled: Union[bool, None] = None
