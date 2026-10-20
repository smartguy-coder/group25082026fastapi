from fastapi import FastAPI


def get_application() -> FastAPI:
    _app = FastAPI()
    return _app


app = get_application()
