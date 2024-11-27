from typing import List, Any

from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

from core.models.db_helper import db_helper
from routers.api.cars.model import (
    read_all_cars as model_read_all_cars,
    read_car as model_read_car, read_cars_human_identify_fields, TABLE_NAME, ID_FIELD_NAME,
)
from routers.api.cars.schemas import Car, CarReadForm
from routers.api.make_models.model import read_make_models_human_identify_fields
from routers.api.owners.model import read_owners_human_identify_fields
from routers.frontend.post_processes import post_process_handler
from routers.frontend.tables.cars.model import get_form_fields
from routers.frontend.tables.model import set_values_for_form_fields
from routers.frontend.tables.schemas import Field, Choice

router = APIRouter(prefix='/cars', tags=['Cars'])

templates = Jinja2Templates(directory='templates')

NAME_PLURAL = 'Cars'
RU_NAME_PLURAL = 'Машины'
LINK_FIELDS = {
    'fk_owner': 'owners',
    'fk_make_model': 'make_models',
    ID_FIELD_NAME: TABLE_NAME,
}
IS_PAGE_ACTIVE_CONDITION_NAME = 'is_cars_active'


@router.get('/create/')
async def create_car(
        request: Request
):
    is_light_theme = request.cookies.get('theme', 'dark') == 'light'

    FORM_FIELDS = await get_form_fields(db_helper)

    level = 4

    context = {
        'level': level,
        'is_tables_active': True,
        IS_PAGE_ACTIVE_CONDITION_NAME: True,
        'is_light_theme': is_light_theme,
        'model': {
            'name_plural': NAME_PLURAL,
            'ru_name_plural': RU_NAME_PLURAL
        },
        'form': {
            'confirm_link': f'api/{TABLE_NAME}/create',
            'fields': FORM_FIELDS,
        }
    }
    print(context['form']['fields'])

    return templates.TemplateResponse(
        request=request,
        name='create_record.html',
        context=context
    )


@router.get('/')
async def read_all_cars(
        request: Request
):
    is_light_theme = request.cookies.get('theme', 'dark') == 'light'
    cars: List[Car] = await model_read_all_cars(db_helper=db_helper)
    await db_helper.commit_and_close()
    cars: List[dict[str, Any]] = [car.model_dump() for car in cars]

    level = 3
    link_fields = {key: f'{"../" * (level - 2)}{value}' for key, value in LINK_FIELDS.items()}

    context = {
        'level': level,
        'is_tables_active': True,
        IS_PAGE_ACTIVE_CONDITION_NAME: True,
        'is_light_theme': is_light_theme,
        'enable_deletes': True,
        'model': {
            'name_plural': NAME_PLURAL,
            'ru_name_plural': RU_NAME_PLURAL,
            'data': cars,
            'fk_fields': link_fields
        }
    }

    return templates.TemplateResponse(
        request=request,
        name='model_read.html',
        context=context
    )


@router.get('/{id_car}/')
async def read_car_by_id(
        request: Request,
        id_car: int,
):
    is_light_theme = request.cookies.get('theme', 'dark') == 'light'
    car: Car = await model_read_car(db_helper=db_helper, car=CarReadForm(id_car=id_car))
    await db_helper.commit_and_close()
    if car is None:
        return None
    cars: List[dict[str, Any]] = [car.model_dump()]

    level = 4
    fk_fields = {key: f'{"../" * (level - 2)}{value}' for key, value in LINK_FIELDS.items()}

    context = {
        'level': level,
        'is_tables_active': True,
        IS_PAGE_ACTIVE_CONDITION_NAME: True,
        'is_light_theme': is_light_theme,
        'model': {
            'name_plural': NAME_PLURAL,
            'table_name': TABLE_NAME,
            'ru_name_plural': RU_NAME_PLURAL,
            'data': cars,
            'fk_fields': fk_fields,
        }
    }

    return templates.TemplateResponse(
        request=request,
        name='model_read_one.html',
        context=context
    )


@router.get('/edit/{instance_id}')
async def update_car(
        request: Request,
        instance_id: int,
):
    form_fields = await get_form_fields(
        db_helper,
        ID_FIELD_NAME=ID_FIELD_NAME,
    )

    instance = await model_read_car(db_helper=db_helper, car=CarReadForm(id_car=instance_id))

    form_fields = await set_values_for_form_fields(
        data=instance,
        fields=form_fields,
        enable_fields=True,
    )

    context = {
        IS_PAGE_ACTIVE_CONDITION_NAME: True,
        'model': {
            'name_plural': NAME_PLURAL,
            'ru_name_plural': RU_NAME_PLURAL
        },
        'form': {
            'confirm_link': f'api/{TABLE_NAME}/update',
            'fields': form_fields,
        }
    }

    return await post_process_handler(request, context)
