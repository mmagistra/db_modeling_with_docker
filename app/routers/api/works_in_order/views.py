from typing import Annotated, List

from fastapi import APIRouter, Form
from starlette import status

from core.models.db_helper import db_helper
from routers.api.works_in_order.model import (
    read_all_works_in_order,
    read_work_in_order,
    create_work_in_order,
    update_work_in_order,
    delete_work_in_order
)
from routers.api.works_in_order.schemas import (
    WorkInOrderReadForm,
    WorkInOrderCreateForm,
    WorkInOrder,
    WorkInOrderUpdateForm,
    WorkInOrderDeleteForm
)

router = APIRouter(prefix='/works_in_work_in_order', tags=['WorkInOrders'])


@router.get('/read')
async def handler_read_all_works_in_work_in_order():
    data = await read_all_works_in_order(db_helper=db_helper)
    response_forms: List[WorkInOrder] = []
    for work_in_order in data:
        response_forms.append(WorkInOrder(**work_in_order.model_dump()))
    return data


@router.get('/read/{id_work_in_order}')
async def handler_read_work_in_order_by_id(
        id_work_in_order: int
):
    form_data = WorkInOrderReadForm(id_work_in_order=int(id_work_in_order))
    data = await read_work_in_order(db_helper=db_helper, work_in_order=form_data)
    if data is None:
        return data
    response_form = WorkInOrder(**data.model_dump())
    return response_form


@router.post('/create')
async def handler_create_work_in_order(
        form_data: Annotated[WorkInOrderCreateForm, Form()]
):
    await create_work_in_order(db_helper=db_helper, work_in_order=form_data)
    return status.HTTP_201_CREATED


@router.post('/update')
async def handler_update_work_in_order(
        form_data: Annotated[WorkInOrderUpdateForm, Form()]
):
    await update_work_in_order(db_helper=db_helper, work_in_order=form_data)
    return status.HTTP_202_ACCEPTED


@router.post('/delete')
async def handle_delete_work_in_order(
        form_data: Annotated[WorkInOrderDeleteForm, Form()]
):
    await delete_work_in_order(db_helper=db_helper, work_in_order=form_data)
    return status.HTTP_202_ACCEPTED
