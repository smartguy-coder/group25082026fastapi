from fastapi import APIRouter, Request, Form, status, Depends
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from routers.api import register_user, login_user
from routers.dependencies import get_current_user
from routers.utils import set_cookies, delete_cookies

router = APIRouter()

templates = Jinja2Templates(directory='templates')


@router.get("/")
async def index(request: Request, data_from_form: str = '', user_and_tokens: dict = Depends(get_current_user)):
    # print(request.__dict__)
    context = {
        'my_data': 9999999999999999,
        "page_title": 'main page',
        'data_from_form': data_from_form,
        'user': user_and_tokens
    }

    response = templates.TemplateResponse(request=request, name='index.html', context=context)
    set_cookies(response, user_and_tokens)
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
    response = await register_user(email=email, name=name, password=password)

    if response.status_code == status.HTTP_201_CREATED:
        login_response = await login_user(email=email, password=password)
        tokens = login_response.json()

        redirect_response =  RedirectResponse(request.url_for("index"), status_code=status.HTTP_303_SEE_OTHER)
        set_cookies(redirect_response, tokens)
        return redirect_response

    elif response.status_code == status.HTTP_409_CONFLICT:
        context['name'] = name
        context['email'] = email
        context['error_msg'] = "Користувач з даним email вже зареєстрований. Перевірте дані та спробуйте знову"


        response = templates.TemplateResponse(request=request, name='register.html', context=context, status_code=400)
        return response

@router.get("/logout")
async def logout(request: Request):

    redirect_response =  RedirectResponse(request.url_for("index"), status_code=status.HTTP_303_SEE_OTHER)
    delete_cookies(redirect_response)
    return redirect_response