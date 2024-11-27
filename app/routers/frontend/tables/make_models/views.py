from typing import List, Any

from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

from core.models.db_helper import db_helper
from routers.api.make_models.model import (
    read_all_make_models as model_read_all_make_models,
    read_make_model as model_read_make_model,
    TABLE_NAME, ID_FIELD_NAME,
)
from routers.api.make_models.schemas import MakeModel, MakeModelReadForm
from routers.frontend.post_processes import post_process_handler
from routers.frontend.tables.make_models.model import get_form_fields
from routers.frontend.tables.model import set_values_for_form_fields
from routers.frontend.tables.schemas import Field

router = APIRouter(prefix='/make_models', tags=['MakeModels'])

templates = Jinja2Templates(directory='templates')

NAME_PLURAL = 'Make - Models'
RU_NAME_PLURAL = 'Марки - Модели'
LINK_FIELDS = {
    ID_FIELD_NAME: TABLE_NAME,
}
IS_PAGE_ACTIVE_CONDITION_NAME = 'is_make_models_active'


@router.get('/create/')
async def create_make_model(
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
async def read_all_make_models(
        request: Request
):
    is_light_theme = request.cookies.get('theme', 'dark') == 'light'
    make_models: List[MakeModel] = await model_read_all_make_models(db_helper=db_helper)
    await db_helper.commit_and_close()
    make_models: List[dict[str, Any]] = [make_model.model_dump() for make_model in make_models]

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
            'data': make_models,
            'fk_fields': link_fields
        }
    }

    return templates.TemplateResponse(
        request=request,
        name='model_read.html',
        context=context
    )


@router.get('/{id_make_model}/')
async def read_make_model_by_id(
        request: Request,
        id_make_model: int,
):
    is_light_theme = request.cookies.get('theme', 'dark') == 'light'
    make_model: MakeModel = await model_read_make_model(db_helper=db_helper, make_model=MakeModelReadForm(id_make_model=id_make_model))
    await db_helper.commit_and_close()
    if make_model is None:
        return None
    make_models: List[dict[str, Any]] = [make_model.model_dump()]

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
            'data': make_models,
            'fk_fields': fk_fields,
        }
    }

    return templates.TemplateResponse(
        request=request,
        name='model_read_one.html',
        context=context
    )


@router.get('/edit/{instance_id}')
async def update_make_model(
        request: Request,
        instance_id: int,
):
    form_fields = await get_form_fields(
        db_helper,
        ID_FIELD_NAME=ID_FIELD_NAME,
    )

    instance = await model_read_make_model(db_helper=db_helper, make_model=MakeModelReadForm(id_make_model=instance_id))

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
