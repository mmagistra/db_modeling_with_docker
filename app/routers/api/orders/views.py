from typing import Annotated, List

from fastapi import APIRouter, Form
from starlette import status

from core.models.db_helper import db_helper
from routers.api.orders.model import (
    read_all_orders,
    read_order,
    create_order,
    update_order,
    delete_order
)
from routers.api.orders.schemas import (
    OrderReadForm,
    OrderCreateForm,
    Order,
    OrderUpdateForm,
    OrderDeleteForm
)

router = APIRouter(prefix='/orders', tags=['Orders'])


@router.get('/read')
async def handler_read_all_orders():
    data = await read_all_orders(db_helper=db_helper)
    response_forms: List[Order] = []
    for order in data:
        response_forms.append(Order(**order.model_dump()))
    return data


@router.get('/read/{id_order}')
async def handler_read_order_by_id(
        id_order: int
):
    form_data = OrderReadForm(id_order=int(id_order))
    data = await read_order(db_helper=db_helper, order=form_data)
    if data is None:
        return data
    response_form = Order(**data.model_dump())
    return response_form


@router.post('/create')
async def handler_create_order(
        form_data: Annotated[OrderCreateForm, Form()]
):
    await create_order(db_helper=db_helper, order=form_data)
    return status.HTTP_201_CREATED


@router.post('/update')
async def handler_update_order(
        form_data: Annotated[OrderUpdateForm, Form()]
):
    await update_order(db_helper=db_helper, order=form_data)
    return status.HTTP_202_ACCEPTED


@router.post('/delete')
async def handle_delete_order(
        form_data: Annotated[OrderDeleteForm, Form()]
):
    await delete_order(db_helper=db_helper, order=form_data)
    return status.HTTP_202_ACCEPTED
