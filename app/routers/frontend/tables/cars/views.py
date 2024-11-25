from typing import List, Any

from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

from core.models.db_helper import db_helper
from routers.api.cars.model import read_all_cars as model_read_all_cars
from routers.api.cars.schemas import Car

router = APIRouter(prefix='/cars', tags=['Cars'])

templates = Jinja2Templates(directory='templates')


@router.get('/')
async def read_all_cars(
        request: Request
):
    is_light_theme = request.cookies.get('theme', 'dark') == 'light'
    cars: List[Car] = await model_read_all_cars(db_helper=db_helper)
    await db_helper.commit_and_close()
    print(cars)
    cars: List[dict[str, Any]] = [car.model_dump() for car in cars]

    context = {
        'level': 3,
        'is_tables_active': True,
        'is_cars_active': True,
        'is_light_theme': is_light_theme,
        'model': {
            'name-plural': 'Cars',
            'data': cars,
            'fk_fields': {
                'fk_owner': '../owners/',
                'fk_make_model': '../make_model/'
            }
        }
    }

    return templates.TemplateResponse(
        request=request,
        name='model_read.html',
        context=context
    )
