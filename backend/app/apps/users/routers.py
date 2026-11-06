from fastapi import APIRouter, status, Depends, Request, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from apps.dependencies.database import get_async_session
from apps.users.crud import user_manager
from apps.users.schemas import CreateUserSchema, UserBaseSchema
from utils.bs_logging import logger

router_users = APIRouter()


# async def get_67(request: Request):
#     print(request.__dict__)
#     raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='not for you')
#     return 67
#
#
# async def get_5_and_more(six_seven: int = Depends(get_67)):
#     return 5 + six_seven


@router_users.post('/create', status_code=status.HTTP_201_CREATED)
async def create_user(
        new_user: CreateUserSchema,
        # five: int = Depends(get_5_and_more)
        session: AsyncSession = Depends(get_async_session)
) -> UserBaseSchema:
    """creating users)))))))))))))"""
    logger.info(new_user)
    # print('result =', five)
    created_user = await user_manager.create_user(new_user, session)
    return created_user


# @router_users.get('/123')
# def log_test():
#     """creating users)))))))))))))"""
#     logger.error('Something bad happened.')
#     logger.info('Log message with structured logging.', extra={
#         'item': "Orange Soda222",
#         'price': 100.00
#     })
#
#     # 1/0
#     return 2005656
