from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory='templates')


@router.get("/")
async def index(request: Request):
    # print(request.__dict__)
    context = {
        'my_data': 9999999999999999
    }

    response = templates.TemplateResponse(request=request, name='index.html', context=context)
    return response



@router.get("/2")
async def page2(request: Request):
    # print(request.__dict__)
    context = {
        'my_data': 9999999999999999
    }

    response = templates.TemplateResponse(request=request, name='page2.html', context=context)
    return response