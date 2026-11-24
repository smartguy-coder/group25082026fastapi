from fastapi import Request

from routers.api import login_user_with_access_token, get_new_token_pair


async def get_current_user(request: Request) -> dict:
    access_token = request.cookies.get('access_token') or ""
    refresh_token = request.cookies.get('refresh_token') or ""
    user = {}

    if not access_token and not refresh_token:
        return user

    if access_token:
        user = await login_user_with_access_token(access_token)
        print(2222222222222222222222222222222222222222222, user)
        if user:
            return user

    if not refresh_token:
        return user
    print(refresh_token, 88888888888888888888888888888888888)
    new_token_pair = await get_new_token_pair(refresh_token)
    if not "access_token" in new_token_pair:
        return user
    print(999999999999999999999999999999999999)
    user = await login_user_with_access_token(new_token_pair['access_token'])
    user |= new_token_pair

    return user