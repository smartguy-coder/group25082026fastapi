from fastapi import APIRouter

router_users = APIRouter()


@router_users.post('/create')
def create_user():
    """creating users)))))))))))))"""
    return 2005656
