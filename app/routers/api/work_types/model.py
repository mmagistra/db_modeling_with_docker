from typing import Annotated, List

from fastapi import Form

from core.models.db_helper import DatabaseHelper
from routers.api.work_types.schemas import WorkTypeCreateForm, WorkTypeUpdateForm, WorkTypeDeleteForm, WorkTypeReadForm, WorkType


TABLE_NAME = 'work_types'
ID_FIELD_NAME = 'id_work_type'
HUMAN_IDENTIFY_FIELDS = ['id_work_type', 'name']


async def read_work_types_human_identify_fields(
        db_helper: DatabaseHelper,
) -> List[dict]:
    return await db_helper.read_fields(
        TABLE_NAME,
        HUMAN_IDENTIFY_FIELDS,
        ID_FIELD_NAME
    )


async def create_work_type(
        db_helper: DatabaseHelper,
        work_type: Annotated[WorkTypeCreateForm, Form()]
):
    await db_helper.create(TABLE_NAME, work_type)


async def read_all_work_types(
        db_helper: DatabaseHelper
) -> List[WorkType]:
    data = await db_helper.read_all(TABLE_NAME, ID_FIELD_NAME, WorkType)
    return data


async def read_work_type(
        db_helper: DatabaseHelper,
        work_type: WorkTypeReadForm
) -> WorkType:
    data = await db_helper.read(TABLE_NAME, ID_FIELD_NAME, work_type.model_dump()[ID_FIELD_NAME], WorkType)
    return data


async def update_work_type(
        db_helper: DatabaseHelper,
        work_type: WorkTypeUpdateForm,
):
    await db_helper.update(TABLE_NAME, ID_FIELD_NAME, work_type.model_dump()[ID_FIELD_NAME], work_type)


async def delete_work_type(
        db_helper: DatabaseHelper,
        work_type: WorkTypeDeleteForm
):
    await db_helper.delete(TABLE_NAME, ID_FIELD_NAME, work_type.model_dump()[ID_FIELD_NAME])
