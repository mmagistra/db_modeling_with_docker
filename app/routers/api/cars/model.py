from typing import Annotated

from fastapi import Form

from core.models.db_helper import DatabaseHelper
from routers.api.cars.schemas import CarCreateForm, CarUpdateForm, CarDeleteForm, CarReadForm


async def create_car(
        db_helper: DatabaseHelper,
        car: Annotated[CarCreateForm, Form()]
):
    stmt = f"""
    INSERT INTO cars (fk_owner, fk_make_model, release_year, car_number)
    VALUES ({car.fk_owner}, {car.fk_make_model}, {car.release_year}, '{car.car_number}')
    """
    await db_helper.execute(stmt)
    await db_helper.commit_and_close()


async def read_all_cars(
        db_helper: DatabaseHelper
):
    stmt = """SELECT * FROM cars ORDER BY id_car"""
    data = await db_helper.query(stmt)
    return data


async def read_car(
        db_helper: DatabaseHelper,
        car: CarReadForm
):
    stmt = f"""SELECT * FROM cars WHERE id_car = {car.id_car} ORDER BY id_car"""
    data = await db_helper.query_first(stmt)
    return data


async def update_car(
        db_helper: DatabaseHelper,
        car: CarUpdateForm,
):
    stmt = f"""
    UPDATE cars
    SET """
    for key, value in car.model_dump().items():
        if value is not None:
            stmt += f"{key}='{value}', "

    if stmt[-2:] == ', ':
        stmt = stmt[:-2]

    stmt += f""" 
    WHERE id_car={car.id_car}
"""

    await db_helper.execute(stmt)
    await db_helper.commit_and_close()


async def delete_car(
        db_helper: DatabaseHelper,
        car: CarDeleteForm
):
    stmt = f"""
    DELETE FROM cars WHERE id_car={car.id_car}
    """
    await db_helper.execute(stmt)
    await db_helper.commit_and_close()
