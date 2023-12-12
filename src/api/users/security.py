from typing import Annotated
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from src.api.users.user_schema import User

oauth2_scheme: OAuth2PasswordBearer = OAuth2PasswordBearer(tokenUrl="token")


def fake_decode_token(token: str) -> User:
    return User(
        username=token + "fakedecoded", email="john@appleseed.com", full_name="John Doe"
    )


def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    user = fake_decode_token(token)
    return user

def fake_hash_password():
    pass

