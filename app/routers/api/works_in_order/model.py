from typing import Annotated

from fastapi import Form

from core.models.db_helper import DatabaseHelper
from routers.api.works_in_order.schemas import WorkInOrderCreateForm, WorkInOrderUpdateForm, WorkInOrderDeleteForm, WorkInOrderReadForm


async def create_work_in_order(
        db_helper: DatabaseHelper,
        work_in_order: Annotated[WorkInOrderCreateForm, Form()]
):
    stmt = f"""
    INSERT INTO works_in_order (fk_order, fk_work_type, work_number, count, amount)
    VALUES (
        {work_in_order.fk_order}, 
        {work_in_order.fk_work_type}, 
        {work_in_order.work_number}, 
        {work_in_order.count}, 
        {work_in_order.amount}
    )
    """
    await db_helper.execute(stmt)
    await db_helper.commit_and_close()


async def read_all_works_in_order(
        db_helper: DatabaseHelper
):
    stmt = """SELECT * FROM works_in_order ORDER BY id_work_in_order"""
    data = await db_helper.query(stmt)
    return data


async def read_work_in_order(
        db_helper: DatabaseHelper,
        work_in_order: WorkInOrderReadForm
):
    stmt = f"""SELECT * FROM works_in_order
        WHERE id_work_in_order = {work_in_order.id_work_in_order} ORDER BY id_work_in_order
    """
    data = await db_helper.query_first(stmt)
    return data


async def update_work_in_order(
        db_helper: DatabaseHelper,
        work_in_order: WorkInOrderUpdateForm,
):
    stmt = f"""
    UPDATE works_in_order
    SET """
    for key, value in work_in_order.model_dump().items():
        if value is not None:
            stmt += f"{key}='{value}', "

    if stmt[-2:] == ', ':
        stmt = stmt[:-2]

    stmt += f""" 
    WHERE id_work_in_order={work_in_order.id_work_in_order}
"""

    await db_helper.execute(stmt)
    await db_helper.commit_and_close()


async def delete_work_in_order(
        db_helper: DatabaseHelper,
        work_in_order: WorkInOrderDeleteForm
):
    stmt = f"""
    DELETE FROM works_in_order WHERE id_work_in_order={work_in_order.id_work_in_order}
    """
    await db_helper.execute(stmt)
    await db_helper.commit_and_close()
