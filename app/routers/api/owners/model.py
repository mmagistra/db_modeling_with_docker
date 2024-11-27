from typing import Annotated, List

from fastapi import Form

from core.models.db_helper import DatabaseHelper
from routers.api.owners.schemas import OwnerCreateForm, OwnerUpdateForm, OwnerDeleteForm, OwnerReadForm, Owner


TABLE_NAME = 'owners'
ID_FIELD_NAME = 'id_owner'
HUMAN_IDENTIFY_FIELDS = ['id_owner', 'name']


async def read_owners_human_identify_fields(
        db_helper: DatabaseHelper,
) -> List[dict]:
    return await db_helper.read_fields(
        TABLE_NAME,
        HUMAN_IDENTIFY_FIELDS,
        ID_FIELD_NAME
    )


async def create_owner(
        db_helper: DatabaseHelper,
        owner: Annotated[OwnerCreateForm, Form()]
):
    await db_helper.create(TABLE_NAME, owner)


async def read_all_owners(
        db_helper: DatabaseHelper
) -> List[Owner]:
    data = await db_helper.read_all(TABLE_NAME, ID_FIELD_NAME, Owner)
    return data


async def read_owner(
        db_helper: DatabaseHelper,
        owner: OwnerReadForm
) -> Owner:
    data = await db_helper.read(TABLE_NAME, ID_FIELD_NAME, owner.model_dump()[ID_FIELD_NAME], Owner)
    return data


async def update_owner(
        db_helper: DatabaseHelper,
        owner: OwnerUpdateForm,
):
    await db_helper.update(TABLE_NAME, ID_FIELD_NAME, owner.model_dump()[ID_FIELD_NAME], owner)


async def delete_owner(
        db_helper: DatabaseHelper,
        owner: OwnerDeleteForm
):
    await db_helper.delete(TABLE_NAME, ID_FIELD_NAME, owner.model_dump()[ID_FIELD_NAME])
