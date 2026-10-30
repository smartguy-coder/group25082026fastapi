from fastapi import FastAPI

from settings import settings
from apps.users.routers import router_users
import sentry_sdk

sentry_sdk.init(
    dsn=settings.SENTRY_DNS,
)


def get_application() -> FastAPI:
    _app = FastAPI(
        title='backend new',
        root_path='/api',
        debug=settings.DEBUG
    )

    _app.include_router(router_users, prefix='/users', tags=['Users'])

    return _app


app = get_application()
