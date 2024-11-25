from typing import Annotated, List

from fastapi import Form

from core.models.db_helper import DatabaseHelper
from routers.api.cars.schemas import CarCreateForm, CarUpdateForm, CarDeleteForm, CarReadForm, Car


TABLE_NAME = 'cars'
ID_FIELD_NAME = 'id_car'


async def create_car(
        db_helper: DatabaseHelper,
        car: Annotated[CarCreateForm, Form()]
):
    await db_helper.create(TABLE_NAME, car)


async def read_all_cars(
        db_helper: DatabaseHelper
) -> List[Car]:
    data = await db_helper.read_all(TABLE_NAME, ID_FIELD_NAME, Car)
    return data


async def read_car(
        db_helper: DatabaseHelper,
        car: CarReadForm
) -> Car:
    data = await db_helper.read(TABLE_NAME, ID_FIELD_NAME, car.model_dump()[ID_FIELD_NAME], Car)
    return data


async def update_car(
        db_helper: DatabaseHelper,
        car: CarUpdateForm,
):
    await db_helper.update(TABLE_NAME, ID_FIELD_NAME, car.model_dump()[ID_FIELD_NAME], car)


async def delete_car(
        db_helper: DatabaseHelper,
        car: CarDeleteForm
):
    await db_helper.delete(TABLE_NAME, ID_FIELD_NAME, car.model_dump()[ID_FIELD_NAME])
