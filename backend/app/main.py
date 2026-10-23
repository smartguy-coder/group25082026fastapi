from fastapi import FastAPI

from apps.users.routers import router_users




def get_application() -> FastAPI:
    _app = FastAPI(
        title='backend new',
        root_path='/api',
    )

    _app.include_router(router_users, prefix='/users', tags=['Users'])

    return _app


app = get_application()
