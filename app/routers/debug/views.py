from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

from core.models.db_helper import db_helper


router = APIRouter(prefix='/debug', tags=['Debug'])

templates = Jinja2Templates(directory='templates')


@router.get("/hello/")
def hello_world():
    return {"message": "Hello World"}


@router.get("/db/")
async def test_db():
    data = await db_helper.query("""SELECT * FROM cars""")
    db_helper.commit_and_close()
    print(data)
    return data


@router.get('/nav')
async def test_nav(
        request: Request
):
    is_light_theme = request.cookies.get('theme', 'dark') == 'light'
    return templates.TemplateResponse(
        request=request,
        name='nav-debug.html',
        context={
            'is_light_theme': is_light_theme,
            'is_accounting_active': True,
            'is_orders_active': True,
        }
    )
