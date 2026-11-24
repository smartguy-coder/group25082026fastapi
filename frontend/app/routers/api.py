import httpx

from settings import settings


async def register_user(*, email: str, name: str, password: str) -> httpx.Response:
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f'{settings.BACKEND_HOST}/api/users/create',
            json={
              "email": email,
              "name": name,
              "password": password
            }
        )
        return response


async def login_user(*, email: str, password: str) -> httpx.Response:
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f'{settings.BACKEND_HOST}/api/auth/login',
            data={
              "username": email,
              "password": password
            }
        )
        return response

async def login_user_with_access_token(access_token: str) -> dict:
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                f'{settings.BACKEND_HOST}/api/users/my-info',
                headers={
                    'Authorization': f"Bearer {access_token}"
                }
            )
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError:
            return {}
        except httpx.RequestError:
            return {}

async def get_new_token_pair(refresh_token: str) -> dict:
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f'{settings.BACKEND_HOST}/api/auth/refresh',
            json={
              "refresh_token": refresh_token,
            }
        )
        print(response.content)

        return response.json()
