from typing import Annotated

from fastapi import Form

from core.models.db_helper import DatabaseHelper
from routers.api.work_types.schemas import WorkTypeCreateForm, WorkTypeUpdateForm, WorkTypeDeleteForm, WorkTypeReadForm


async def create_work_type(
        db_helper: DatabaseHelper,
        work_type: Annotated[WorkTypeCreateForm, Form()]
):
    stmt = f"""
    INSERT INTO work_types (name, price)
    VALUES ('{work_type.name}', {work_type.price})
    """
    await db_helper.execute(stmt)
    await db_helper.commit_and_close()


async def read_all_work_types(
        db_helper: DatabaseHelper
):
    stmt = """SELECT * FROM work_types ORDER BY id_work_type"""
    data = await db_helper.query(stmt)
    return data


async def read_work_type(
        db_helper: DatabaseHelper,
        work_type: WorkTypeReadForm
):
    stmt = f"""SELECT * FROM work_types WHERE id_work_type = {work_type.id_work_type} ORDER BY id_work_type"""
    data = await db_helper.query_first(stmt)
    return data


async def update_work_type(
        db_helper: DatabaseHelper,
        work_type: WorkTypeUpdateForm,
):
    stmt = f"""
    UPDATE work_types
    SET """
    for key, value in work_type.model_dump().items():
        if value is not None:
            stmt += f"{key}='{value}', "

    if stmt[-2:] == ', ':
        stmt = stmt[:-2]

    stmt += f""" 
    WHERE id_work_type={work_type.id_work_type}
"""

    await db_helper.execute(stmt)
    await db_helper.commit_and_close()


async def delete_work_type(
        db_helper: DatabaseHelper,
        work_type: WorkTypeDeleteForm
):
    stmt = f"""
    DELETE FROM work_types WHERE id_work_type={work_type.id_work_type}
    """
    await db_helper.execute(stmt)
    await db_helper.commit_and_close()
