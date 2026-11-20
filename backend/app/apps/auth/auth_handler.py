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
            access_token=self.create_access_token(user),
            refresh_token=self.create_refresh_token(user),
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


    def create_access_token(self, user: User) -> str:
        token = self.create_jwt_token(
            payload={'id': user.id, 'email': user.email, "type": "access_token"},
            expire_minutes=5
        )
        return token


    def create_refresh_token(self, user: User) -> str:
        token = self.create_jwt_token(
            payload={'id': user.id, 'email': user.email, "type": "refresh_token"},
            expire_minutes=60
        )
        return token


auth_handler = AuthHandler()
