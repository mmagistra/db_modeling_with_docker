from typing import List, Any

from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

from core.models.db_helper import db_helper
from routers.api.orders.model import read_orders_human_identify_fields
from routers.api.orders.model import (
    read_all_orders as model_read_all_orders,
    read_order as model_read_order, TABLE_NAME, ID_FIELD_NAME,
)
from routers.api.orders.schemas import Order, OrderReadForm
from routers.frontend.post_processes import post_process_handler
from routers.frontend.tables.model import set_values_for_form_fields
from routers.frontend.tables.orders.model import get_form_fields
from routers.frontend.tables.schemas import Choice, Field

router = APIRouter(prefix='/orders', tags=['Orders'])

templates = Jinja2Templates(directory='templates')

NAME_PLURAL = 'Orders'
RU_NAME_PLURAL = 'Заказы'
LINK_FIELDS = {
    'fk_car': 'cars',
    ID_FIELD_NAME: TABLE_NAME,
}
IS_PAGE_ACTIVE_CONDITION_NAME = 'is_orders_active'


@router.get('/create/')
async def create_order(
        request: Request
):
    is_light_theme = request.cookies.get('theme', 'dark') == 'light'

    FORM_FIELDS = get_form_fields(db_helper)

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

    return templates.TemplateResponse(
        request=request,
        name='create_record.html',
        context=context
    )


@router.get('/')
async def read_all_orders(
        request: Request
):
    is_light_theme = request.cookies.get('theme', 'dark') == 'light'
    orders: List[Order] = await model_read_all_orders(db_helper=db_helper)
    await db_helper.commit_and_close()
    orders: List[dict[str, Any]] = [order.model_dump() for order in orders]

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
            'data': orders,
            'fk_fields': link_fields
        }
    }

    return templates.TemplateResponse(
        request=request,
        name='model_read.html',
        context=context
    )


@router.get('/{id_order}/')
async def read_order_by_id(
        request: Request,
        id_order: int,
):
    is_light_theme = request.cookies.get('theme', 'dark') == 'light'
    order: Order = await model_read_order(db_helper=db_helper, order=OrderReadForm(id_order=id_order))
    await db_helper.commit_and_close()
    if order is None:
        return None
    orders: List[dict[str, Any]] = [order.model_dump()]

    level = 4
    fk_fields = {key: f'{"../" * (level - 2)}{value}' for key, value in LINK_FIELDS.items()}

    context = {
        'level': level,
        'is_tables_active': True,
        IS_PAGE_ACTIVE_CONDITION_NAME: True,
        'is_light_theme': is_light_theme,
        'model': {
            'name_plural': NAME_PLURAL,
            'ru_name_plural': RU_NAME_PLURAL,
            'table_name': TABLE_NAME,
            'data': orders,
            'fk_fields': fk_fields,
        }
    }

    return templates.TemplateResponse(
        request=request,
        name='model_read_one.html',
        context=context
    )


@router.get('/edit/{instance_id}')
async def update_order(
        request: Request,
        instance_id: int,
):
    form_fields = await get_form_fields(
        db_helper,
        ID_FIELD_NAME=ID_FIELD_NAME,
    )

    instance = await model_read_order(db_helper=db_helper, order=OrderReadForm(id_order=instance_id))

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
