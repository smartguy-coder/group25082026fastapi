from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from apps.auth.auth_handler import auth_handler
from apps.dependencies.database import get_async_session
from apps.users.models import User
from fastapi.security import OAuth2PasswordBearer


class SecurityHandler:
    oauth2_schema = OAuth2PasswordBearer(tokenUrl="/api/auth/login")


async def get_current_user(
        token: str = Depends(SecurityHandler.oauth2_schema),
        session: AsyncSession = Depends(get_async_session)
) -> User:
    payload = auth_handler.decode_token(token)
    if not payload['type'] == 'access_token':
        raise HTTPException(detail='Invalid token type', status_code=status.HTTP_400_BAD_REQUEST)

