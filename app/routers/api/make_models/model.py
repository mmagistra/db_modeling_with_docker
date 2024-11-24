from typing import Annotated

from fastapi import Form

from core.models.db_helper import DatabaseHelper
from routers.api.make_models.schemas import MakeModelCreateForm, MakeModelUpdateForm, MakeModelDeleteForm, MakeModelReadForm


async def create_make_model(
        db_helper: DatabaseHelper,
        make_model: Annotated[MakeModelCreateForm, Form()]
):
    stmt = f"""
    INSERT INTO make_models (make_model)
    VALUES ('{make_model.make_model}')
    """
    await db_helper.execute(stmt)
    await db_helper.commit_and_close()


async def read_all_make_models(
        db_helper: DatabaseHelper
):
    stmt = """SELECT * FROM make_models ORDER BY id_make_model"""
    data = await db_helper.query(stmt)
    return data


async def read_make_model(
        db_helper: DatabaseHelper,
        make_model: MakeModelReadForm
):
    stmt = f"""SELECT * FROM make_models WHERE id_make_model = {make_model.id_make_model} ORDER BY id_make_model"""
    data = await db_helper.query_first(stmt)
    return data


async def update_make_model(
        db_helper: DatabaseHelper,
        make_model: MakeModelUpdateForm,
):
    stmt = f"""
    UPDATE make_models
    SET """
    for key, value in make_model.model_dump().items():
        if value is not None:
            stmt += f"{key}='{value}', "

    if stmt[-2:] == ', ':
        stmt = stmt[:-2]

    stmt += f""" 
    WHERE id_make_model={make_model.id_make_model}
"""

    await db_helper.execute(stmt)
    await db_helper.commit_and_close()


async def delete_make_model(
        db_helper: DatabaseHelper,
        make_model: MakeModelDeleteForm
):
    stmt = f"""
    DELETE FROM make_models WHERE id_make_model={make_model.id_make_model}
    """
    await db_helper.execute(stmt)
    await db_helper.commit_and_close()
