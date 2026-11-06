from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status

from apps.core.security import PasswordHandler
from apps.users.models import User
from apps.users.schemas import CreateUserSchema
from sqlalchemy.exc import IntegrityError


class UserDBManager:

    async def create_user(self, new_user: CreateUserSchema, session: AsyncSession):

        user = User(
            email=new_user.email.lower(),
            hashed_password=PasswordHandler.get_password_hash(new_user.password),
            name=new_user.name
        )
        session.add(user)
        try:
            await session.commit()
            return user
        except IntegrityError:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f'user with email {new_user.email} already exists'
            )


user_manager = UserDBManager()
