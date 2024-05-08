from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from src.models import User
from src.utils import parse_access_token

security = HTTPBearer()


async def get_user(credentials: Annotated[HTTPAuthorizationCredentials, Depends(security)]) -> User:
    user_id = parse_access_token(credentials.credentials)

    if user_id is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    user = await User.get_or_none(id=user_id)

    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    return user
