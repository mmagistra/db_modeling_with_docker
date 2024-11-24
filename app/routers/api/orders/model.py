from typing import Annotated

from fastapi import Form

from core.models.db_helper import DatabaseHelper
from routers.api.orders.schemas import OrderCreateForm, OrderUpdateForm, OrderDeleteForm, OrderReadForm


async def create_order(
        db_helper: DatabaseHelper,
        order: Annotated[OrderCreateForm, Form()]
):
    stmt = f"""
    INSERT INTO orders (date, fk_car)
    VALUES ('{order.date}', {order.fk_car})
    """
    await db_helper.execute(stmt)
    await db_helper.commit_and_close()


async def read_all_orders(
        db_helper: DatabaseHelper
):
    stmt = """SELECT * FROM orders ORDER BY id_order"""
    data = await db_helper.query(stmt)
    return data


async def read_order(
        db_helper: DatabaseHelper,
        order: OrderReadForm
):
    stmt = f"""SELECT * FROM orders WHERE id_order = {order.id_order} ORDER BY id_order"""
    data = await db_helper.query_first(stmt)
    return data


async def update_order(
        db_helper: DatabaseHelper,
        order: OrderUpdateForm,
):
    stmt = f"""
    UPDATE orders
    SET """
    for key, value in order.model_dump().items():
        if value is not None:
            stmt += f"{key}='{value}', "

    if stmt[-2:] == ', ':
        stmt = stmt[:-2]

    stmt += f""" 
    WHERE id_order={order.id_order}
"""

    await db_helper.execute(stmt)
    await db_helper.commit_and_close()


async def delete_order(
        db_helper: DatabaseHelper,
        order: OrderDeleteForm
):
    stmt = f"""
    DELETE FROM orders WHERE id_order={order.id_order}
    """
    await db_helper.execute(stmt)
    await db_helper.commit_and_close()
