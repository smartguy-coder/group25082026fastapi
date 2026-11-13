from fastapi import APIRouter, Request, Form, status
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
import httpx
import json

router = APIRouter()

templates = Jinja2Templates(directory='templates')


@router.get("/")
async def index(request: Request, data_from_form: str = ''):
    print(request.__dict__)
    context = {
        'my_data': 9999999999999999,
        "page_title": 'main page',
        'data_from_form': data_from_form

    }

    response = templates.TemplateResponse(request=request, name='index.html', context=context)
    return response


@router.post("/register")
@router.get("/register")
async def register(request: Request, email: str = Form(""), name: str = Form(""), password: str = Form("")):
    # print(request.__dict__)

    context = {
        "page_title": 'register'
    }
    if request.method == "GET":
        response = templates.TemplateResponse(request=request, name='register.html', context=context)
        return response

    # POST
    async with httpx.AsyncClient() as client:
        response = await client.post(
            'http://backend:8000/api/users/create',
            json={
              "email": email,
              "name": name,
              "password": password
            }
        )

    if response.status_code == status.HTTP_201_CREATED:
        return RedirectResponse(request.url_for("index"), status_code=status.HTTP_303_SEE_OTHER)

    elif response.status_code == status.HTTP_409_CONFLICT:
        context['name'] = name
        context['email'] = email
        context['error_msg'] = "Користувач з даним email вже зареєстрований. Перевірте дані та спробуйте знову"


        response = templates.TemplateResponse(request=request, name='register.html', context=context, status_code=400)
        return response

