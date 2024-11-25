from typing import Annotated, List

from fastapi import Form

from core.models.db_helper import DatabaseHelper
from routers.api.works_in_order.schemas import WorkInOrderCreateForm, WorkInOrderUpdateForm, WorkInOrderDeleteForm, WorkInOrderReadForm, WorkInOrder


TABLE_NAME = 'works_in_order'
ID_FIELD_NAME = 'id_work_in_order'


async def create_work_in_order(
        db_helper: DatabaseHelper,
        work_in_order: Annotated[WorkInOrderCreateForm, Form()]
):
    await db_helper.create(TABLE_NAME, work_in_order)


async def read_all_works_in_order(
        db_helper: DatabaseHelper
) -> List[WorkInOrder]:
    data = await db_helper.read_all(TABLE_NAME, ID_FIELD_NAME, WorkInOrder)
    return data


async def read_work_in_order(
        db_helper: DatabaseHelper,
        work_in_order: WorkInOrderReadForm
) -> WorkInOrder:
    data = await db_helper.read(TABLE_NAME, ID_FIELD_NAME, work_in_order.model_dump()[ID_FIELD_NAME], WorkInOrder)
    return data


async def update_work_in_order(
        db_helper: DatabaseHelper,
        work_in_order: WorkInOrderUpdateForm,
):
    await db_helper.update(TABLE_NAME, ID_FIELD_NAME, work_in_order.model_dump()[ID_FIELD_NAME], work_in_order)


async def delete_work_in_order(
        db_helper: DatabaseHelper,
        work_in_order: WorkInOrderDeleteForm
):
    await db_helper.delete(TABLE_NAME, ID_FIELD_NAME, work_in_order.model_dump()[ID_FIELD_NAME])
