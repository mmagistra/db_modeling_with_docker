from typing import Annotated, List

from fastapi import APIRouter, Form
from starlette import status

from core.models.db_helper import db_helper
from routers.api.work_types.model import (
    read_all_work_types,
    read_work_type,
    create_work_type,
    update_work_type,
    delete_work_type
)
from routers.api.work_types.schemas import (
    WorkTypeReadForm,
    WorkTypeCreateForm,
    WorkType,
    WorkTypeUpdateForm,
    WorkTypeDeleteForm
)

router = APIRouter(prefix='/work_types', tags=['WorkTypes'])


@router.get('/read')
async def handler_read_all_work_types():
    data = await read_all_work_types(db_helper=db_helper)
    response_forms: List[WorkType] = []
    for work_type in data:
        response_forms.append(WorkType(**work_type.model_dump()))
    return data


@router.get('/read/{id_work_type}')
async def handler_read_work_type_by_id(
        id_work_type: int
):
    form_data = WorkTypeReadForm(id_work_type=int(id_work_type))
    data = await read_work_type(db_helper=db_helper, work_type=form_data)
    if data is None:
        return data
    response_form = WorkType(**data.model_dump())
    return response_form


@router.post('/create')
async def handler_create_work_type(
        form_data: Annotated[WorkTypeCreateForm, Form()]
):
    await create_work_type(db_helper=db_helper, work_type=form_data)
    return status.HTTP_201_CREATED


@router.post('/update')
async def handler_update_work_type(
        form_data: Annotated[WorkTypeUpdateForm, Form()]
):
    await update_work_type(db_helper=db_helper, work_type=form_data)
    return status.HTTP_202_ACCEPTED


@router.post('/delete')
async def handle_delete_work_type(
        form_data: Annotated[WorkTypeDeleteForm, Form()]
):
    await delete_work_type(db_helper=db_helper, work_type=form_data)
    return status.HTTP_202_ACCEPTED
