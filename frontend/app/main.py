from fastapi import FastAPI

from routers.main_page_router import router


def get_application() -> FastAPI:
    _app = FastAPI(
        title='frontend',
        docs_url=None,
        openapi_url=None,

    )
    _app.include_router(router)

    return _app


app = get_application()
