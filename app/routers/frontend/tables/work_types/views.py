from typing import List, Any

from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

from core.models.db_helper import db_helper
from routers.frontend.post_processes import post_process_handler
from routers.api.work_types.model import (
    read_all_work_types as model_read_all_work_types,
    read_work_type as model_read_work_type, TABLE_NAME, ID_FIELD_NAME,
)
from routers.api.work_types.schemas import WorkType, WorkTypeReadForm
from routers.frontend.tables.model import set_values_for_form_fields
from routers.frontend.tables.schemas import Choice, Field
from routers.frontend.tables.work_types.model import get_form_fields

router = APIRouter(prefix='/work_types', tags=['WorkTypess'])

templates = Jinja2Templates(directory='templates')

NAME_PLURAL = 'Work types'
RU_NAME_PLURAL = 'Типы работ'
LINK_FIELDS = {
    ID_FIELD_NAME: TABLE_NAME,
}
IS_PAGE_ACTIVE_CONDITION_NAME = 'is_work_types_active'


@router.get('/create/')
async def create_work_type(
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

    return templates.TemplateResponse(
        request=request,
        name='create_record.html',
        context=context
    )


@router.get('/')
async def read_all_work_types(
        request: Request
):
    is_light_theme = request.cookies.get('theme', 'dark') == 'light'
    work_types: List[WorkType] = await model_read_all_work_types(db_helper=db_helper)
    await db_helper.commit_and_close()
    work_types: List[dict[str, Any]] = [work_type.model_dump() for work_type in work_types]

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
            'data': work_types,
            'fk_fields': link_fields
        }
    }

    return templates.TemplateResponse(
        request=request,
        name='model_read.html',
        context=context
    )


@router.get('/{id_work_type}/')
async def read_work_type_by_id(
        request: Request,
        id_work_type: int,
):
    is_light_theme = request.cookies.get('theme', 'dark') == 'light'
    work_type: WorkType = await model_read_work_type(
        db_helper=db_helper,
        work_type=WorkTypeReadForm(id_work_type=id_work_type)
    )
    await db_helper.commit_and_close()
    if work_type is None:
        return None
    work_types: List[dict[str, Any]] = [work_type.model_dump()]

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
            'data': work_types,
            'fk_fields': fk_fields,
        }
    }

    return templates.TemplateResponse(
        request=request,
        name='model_read_one.html',
        context=context
    )


@router.get('/edit/{instance_id}')
async def update_work_type(
        request: Request,
        instance_id: int,
):
    form_fields = await get_form_fields(
        db_helper,
        ID_FIELD_NAME=ID_FIELD_NAME,
    )

    instance = await model_read_work_type(db_helper=db_helper, work_type=WorkTypeReadForm(id_work_type=instance_id))

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
