import jwt
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status
from apps.auth.schemas import LoginResponseSchema
from apps.core.security import PasswordHandler
from apps.users.crud import user_manager

from datetime import datetime, timedelta
from apps.users.models import User
from settings import settings
from utils.redis_utils import redis_client


class AuthHandler:

    async def get_login_token_pair(
        self,
        data: OAuth2PasswordRequestForm,
        session: AsyncSession
    ) -> LoginResponseSchema:
        user: User | None = await user_manager.get_user(data.username, session)
        if not user:
            raise HTTPException(
                detail=f"User with email '{data.username}' not found",
                status_code=status.HTTP_404_NOT_FOUND
            )

        is_valid_password = PasswordHandler.verify_password(data.password, user.hashed_password)
        if not is_valid_password:
            raise HTTPException(
                detail="Incorrect password",
                status_code=status.HTTP_400_BAD_REQUEST
            )

        return LoginResponseSchema(
            access_token=await self.create_access_token(user),
            refresh_token=await self.create_refresh_token(user),
        )

    async def get_refresh_token_pair(
        self,
        refresh_token: str,
        session: AsyncSession
    ) -> LoginResponseSchema:
        payload = self.decode_token(refresh_token)
        if not payload['type'] == 'refresh_token':
            raise HTTPException(detail='Invalid token type', status_code=status.HTTP_400_BAD_REQUEST)

        user_id = payload['id']

        token_key = f"refresh_tokens:{user_id}"
        stored_refresh = await redis_client.get_cache(token_key)

        if stored_refresh.decode() != refresh_token:
            raise HTTPException(detail='Refresh token was used', status_code=status.HTTP_400_BAD_REQUEST)

        await redis_client.delete_cache(token_key)

        user: User | None = await user_manager.get_user_by_id(user_id=user_id, session=session)

        if not user:
            raise HTTPException(detail='User was not found', status_code=status.HTTP_404_NOT_FOUND)

        return LoginResponseSchema(
            access_token=await self.create_access_token(user),
            refresh_token=await self.create_refresh_token(user),
        )

    def decode_token(self, token: str) -> dict:
        try:
            payload = jwt.decode(token, settings.JWT_SECRET, [settings.JWT_ALGORITHM])
            return payload
        except jwt.ExpiredSignatureError:
            raise HTTPException(
                detail="Token is expired",
                status_code=status.HTTP_401_UNAUTHORIZED
            )
        except jwt.InvalidTokenError:
            raise HTTPException(
                detail="Invalid token",
                status_code=status.HTTP_400_BAD_REQUEST
            )

    def create_jwt_token(self, payload: dict, expire_minutes: int) -> str:
        now = datetime.now()
        expire_delta = timedelta(minutes=expire_minutes)
        time_payload = {
            "exp": now + expire_delta,
            "iat": now
        }
        payload.update(time_payload)
        token = jwt.encode(payload, settings.JWT_SECRET, settings.JWT_ALGORITHM)
        return token


    async def create_access_token(self, user: User) -> str:
        token = self.create_jwt_token(
            payload={'id': user.id, 'email': user.email, "type": "access_token"},
            expire_minutes=15
        )
        return token


    async def create_refresh_token(self, user: User) -> str:
        expire_minutes = 60
        token = self.create_jwt_token(
            payload={'id': user.id, 'email': user.email, "type": "refresh_token"},
            expire_minutes=expire_minutes
        )

        await redis_client.set_cache(f"refresh_tokens:{user.id}", token, expire_minutes * 60)
        return token


auth_handler = AuthHandler()
