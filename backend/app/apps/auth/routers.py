from fastapi import APIRouter, status, Depends, Request, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from apps.auth.auth_handler import auth_handler
from apps.auth.schemas import LoginResponseSchema
from apps.dependencies.database import get_async_session
from sqlalchemy.ext.asyncio import AsyncSession


router_auth = APIRouter()


@router_auth.post("/login")
async def user_login(
    data: OAuth2PasswordRequestForm = Depends(),
    session: AsyncSession = Depends(get_async_session)
) -> LoginResponseSchema:
    print(data.password, data.username)
    response = await auth_handler.get_login_token_pair(data, session)
    return response
