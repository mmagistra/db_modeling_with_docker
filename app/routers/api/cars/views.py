from typing import Annotated, List

from fastapi import APIRouter, Form
from starlette import status

from core.models.db_helper import db_helper
from routers.api.cars.model import (
    read_all_cars,
    read_car,
    create_car,
    update_car,
    delete_car
)
from routers.api.cars.schemas import (
    CarReadForm,
    CarCreateForm,
    Car,
    CarUpdateForm,
    CarDeleteForm
)

router = APIRouter(prefix='/cars', tags=['Cars'])


@router.get('/read')
async def handler_read_all_cars():
    data = await read_all_cars(db_helper=db_helper)
    response_forms: List[Car] = []
    for car in data:
        response_forms.append(Car(**car.model_dump()))
    return data


@router.get('/read/{id_car}')
async def handler_read_car_by_id(
        id_car: int
):
    form_data = CarReadForm(id_car=int(id_car))
    data = await read_car(db_helper=db_helper, car=form_data)
    if data is None:
        return data
    response_form = Car(**data.model_dump())
    return response_form


@router.post('/create')
async def handler_create_car(
        form_data: Annotated[CarCreateForm, Form()]
):
    await create_car(db_helper=db_helper, car=form_data)
    return status.HTTP_201_CREATED


@router.post('/update')
async def handler_update_car(
        form_data: Annotated[CarUpdateForm, Form()]
):
    await update_car(db_helper=db_helper, car=form_data)
    return status.HTTP_202_ACCEPTED


@router.post('/delete')
async def handle_delete_car(
        form_data: Annotated[CarDeleteForm, Form()]
):
    await delete_car(db_helper=db_helper, car=form_data)
    return status.HTTP_202_ACCEPTED
