from fastapi import APIRouter, status

from apps.users.schemas import CreateUserSchema, UserBaseSchema
from utils.bs_logging import logger

router_users = APIRouter()


@router_users.post('/create', status_code=status.HTTP_201_CREATED)
async def create_user(new_user: CreateUserSchema) -> UserBaseSchema:
    """creating users)))))))))))))"""
    logger.info(new_user)
    # todo save user in db
    return new_user

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
