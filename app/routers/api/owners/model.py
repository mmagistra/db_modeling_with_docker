from typing import Annotated

from fastapi import Form

from core.models.db_helper import DatabaseHelper
from routers.api.owners.schemas import OwnerCreateForm, OwnerUpdateForm, OwnerDeleteForm, OwnerReadForm


async def create_owner(
        db_helper: DatabaseHelper,
        owner: Annotated[OwnerCreateForm, Form()]
):
    stmt = f"""
    INSERT INTO owners (name, phone_number)
    VALUES ('{owner.name}', {owner.phone_number})
    """
    await db_helper.execute(stmt)
    await db_helper.commit_and_close()


async def read_all_owners(
        db_helper: DatabaseHelper
):
    stmt = """SELECT * FROM owners ORDER BY id_owner"""
    data = await db_helper.query(stmt)
    return data


async def read_owner(
        db_helper: DatabaseHelper,
        owner: OwnerReadForm
):
    stmt = f"""SELECT * FROM owners WHERE id_owner = {owner.id_owner} ORDER BY id_owner"""
    data = await db_helper.query_first(stmt)
    return data


async def update_owner(
        db_helper: DatabaseHelper,
        owner: OwnerUpdateForm,
):
    stmt = f"""
    UPDATE owners
    SET """
    for key, value in owner.model_dump().items():
        if value is not None:
            stmt += f"{key}='{value}', "

    if stmt[-2:] == ', ':
        stmt = stmt[:-2]

    stmt += f""" 
    WHERE id_owner={owner.id_owner}
"""

    await db_helper.execute(stmt)
    await db_helper.commit_and_close()


async def delete_owner(
        db_helper: DatabaseHelper,
        owner: OwnerDeleteForm
):
    stmt = f"""
    DELETE FROM owners WHERE id_owner={owner.id_owner}
    """
    await db_helper.execute(stmt)
    await db_helper.commit_and_close()
