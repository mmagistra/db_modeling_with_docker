from typing import Annotated, List

from fastapi import Form

from core.models.db_helper import DatabaseHelper
from routers.api.orders.schemas import OrderCreateForm, OrderUpdateForm, OrderDeleteForm, OrderReadForm, Order


TABLE_NAME = 'orders'
ID_FIELD_NAME = 'id_order'
HUMAN_IDENTIFY_FIELDS = ['id_order', 'date', 'car_number']
HUMAN_IDENTIFY_ADDITIONAL_TABLES = [
    {
        'inner_id': 'orders.fk_car',
        'outer_id': 'cars.id_car',
        'table_to_join': 'cars'
     }
]


async def read_orders_human_identify_fields(
        db_helper: DatabaseHelper,
) -> List[dict]:
    return await db_helper.read_fields(
        TABLE_NAME,
        HUMAN_IDENTIFY_FIELDS,
        ID_FIELD_NAME,
        HUMAN_IDENTIFY_ADDITIONAL_TABLES
    )


async def create_order(
        db_helper: DatabaseHelper,
        order: Annotated[OrderCreateForm, Form()]
):
    await db_helper.create(TABLE_NAME, order)


async def read_all_orders(
        db_helper: DatabaseHelper
) -> List[Order]:
    data = await db_helper.read_all(TABLE_NAME, ID_FIELD_NAME, Order)
    return data


async def read_order(
        db_helper: DatabaseHelper,
        order: OrderReadForm
) -> Order:
    data = await db_helper.read(TABLE_NAME, ID_FIELD_NAME, order.model_dump()[ID_FIELD_NAME], Order)
    return data


async def update_order(
        db_helper: DatabaseHelper,
        order: OrderUpdateForm,
):
    await db_helper.update(TABLE_NAME, ID_FIELD_NAME, order.model_dump()[ID_FIELD_NAME], order)


async def delete_order(
        db_helper: DatabaseHelper,
        order: OrderDeleteForm
):
    await db_helper.delete(TABLE_NAME, ID_FIELD_NAME, order.model_dump()[ID_FIELD_NAME])
