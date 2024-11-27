from typing import Annotated, List

from fastapi import Form

from core.models.db_helper import DatabaseHelper
from routers.api.make_models.schemas import MakeModelCreateForm, MakeModelUpdateForm, MakeModelDeleteForm, MakeModelReadForm, MakeModel


TABLE_NAME = 'make_models'
ID_FIELD_NAME = 'id_make_model'
HUMAN_IDENTIFY_FIELDS = ['id_make_model', 'make_model']


async def read_make_models_human_identify_fields(
        db_helper: DatabaseHelper,
) -> List[dict]:
    return await db_helper.read_fields(TABLE_NAME, HUMAN_IDENTIFY_FIELDS, ID_FIELD_NAME)


async def create_make_model(
        db_helper: DatabaseHelper,
        make_model: Annotated[MakeModelCreateForm, Form()]
):
    await db_helper.create(TABLE_NAME, make_model)


async def read_all_make_models(
        db_helper: DatabaseHelper
) -> List[MakeModel]:
    data = await db_helper.read_all(TABLE_NAME, ID_FIELD_NAME, MakeModel)
    return data


async def read_make_model(
        db_helper: DatabaseHelper,
        make_model: MakeModelReadForm
) -> MakeModel:
    data = await db_helper.read(TABLE_NAME, ID_FIELD_NAME, make_model.model_dump()[ID_FIELD_NAME], MakeModel)
    return data


async def update_make_model(
        db_helper: DatabaseHelper,
        make_model: MakeModelUpdateForm,
):
    await db_helper.update(TABLE_NAME, ID_FIELD_NAME, make_model.model_dump()[ID_FIELD_NAME], make_model)


async def delete_make_model(
        db_helper: DatabaseHelper,
        make_model: MakeModelDeleteForm
):
    await db_helper.delete(TABLE_NAME, ID_FIELD_NAME, make_model.model_dump()[ID_FIELD_NAME])
