from typing import List, Any

from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

from core.models.db_helper import db_helper
from routers.api.owners.model import (
    read_all_owners as model_read_all_owners,
    read_owner as model_read_owner, read_owners_human_identify_fields, TABLE_NAME, ID_FIELD_NAME,
)
from routers.api.owners.schemas import Owner, OwnerReadForm
from routers.frontend.post_processes import post_process_handler
from routers.frontend.tables.model import set_values_for_form_fields
from routers.frontend.tables.owners.model import get_form_fields
from routers.frontend.tables.schemas import Choice, Field

router = APIRouter(prefix='/owners', tags=['Owners'])

templates = Jinja2Templates(directory='templates')

NAME_PLURAL = 'Owners'
RU_NAME_PLURAL = 'Владельцы'
LINK_FIELDS = {
    ID_FIELD_NAME: TABLE_NAME,
}
IS_PAGE_ACTIVE_CONDITION_NAME = 'is_owners_active'


@router.get('/create/')
async def create_owner(
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
async def read_all_owners(
        request: Request
):
    is_light_theme = request.cookies.get('theme', 'dark') == 'light'
    owners: List[Owner] = await model_read_all_owners(db_helper=db_helper)
    await db_helper.commit_and_close()
    owners: List[dict[str, Any]] = [owner.model_dump() for owner in owners]

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
            'data': owners,
            'fk_fields': link_fields
        }
    }

    return templates.TemplateResponse(
        request=request,
        name='model_read.html',
        context=context
    )


@router.get('/{id_owner}/')
async def read_owner_by_id(
        request: Request,
        id_owner: int,
):
    is_light_theme = request.cookies.get('theme', 'dark') == 'light'
    owner: Owner = await model_read_owner(db_helper=db_helper, owner=OwnerReadForm(id_owner=id_owner))
    await db_helper.commit_and_close()
    if owner is None:
        return None
    owners: List[dict[str, Any]] = [owner.model_dump()]

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
            'data': owners,
            'fk_fields': fk_fields,
        }
    }

    return templates.TemplateResponse(
        request=request,
        name='model_read_one.html',
        context=context
    )


@router.get('/edit/{instance_id}')
async def update_owner(
        request: Request,
        instance_id: int,
):
    form_fields = await get_form_fields(
        db_helper,
        ID_FIELD_NAME=ID_FIELD_NAME,
    )

    instance = await model_read_owner(db_helper=db_helper, owner=OwnerReadForm(id_owner=instance_id))

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
