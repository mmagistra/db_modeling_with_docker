from typing import Annotated, List

from fastapi import APIRouter, Form
from starlette import status

from core.models.db_helper import db_helper
from routers.api.make_models.model import (
    read_all_make_models,
    read_make_model,
    create_make_model,
    update_make_model,
    delete_make_model
)
from routers.api.make_models.schemas import (
    MakeModelReadForm,
    MakeModelCreateForm,
    MakeModel,
    MakeModelUpdateForm,
    MakeModelDeleteForm
)

router = APIRouter(prefix='/make_models', tags=['MakeModel'])


@router.get('/read')
async def handler_read_all_make_models():
    data = await read_all_make_models(db_helper=db_helper)
    response_forms: List[MakeModel] = []
    for make_model in data:
        response_forms.append(MakeModel(**make_model.model_dump()))
    return data


@router.get('/read/{id_make_model}')
async def handler_read_make_model_by_id(
        id_make_model: int
):
    form_data = MakeModelReadForm(id_make_model=int(id_make_model))
    data = await read_make_model(db_helper=db_helper, make_model=form_data)
    if data is None:
        return data
    response_form = MakeModel(**data.model_dump())
    return response_form


@router.post('/create')
async def handler_create_make_model(
        form_data: Annotated[MakeModelCreateForm, Form()]
):
    await create_make_model(db_helper=db_helper, make_model=form_data)
    return status.HTTP_201_CREATED


@router.post('/update')
async def handler_update_make_model(
        form_data: Annotated[MakeModelUpdateForm, Form()]
):
    await update_make_model(db_helper=db_helper, make_model=form_data)
    return status.HTTP_202_ACCEPTED


@router.post('/delete')
async def handle_delete_car_with_form(
        form_data: Annotated[MakeModelDeleteForm, Form()]
):
    await delete_make_model(db_helper=db_helper, make_model=form_data)
    return status.HTTP_202_ACCEPTED


@router.post('/delete/{id_for_delete}')
async def handle_delete_car_with_query(
        id_for_delete: int
):
    form_data = MakeModelDeleteForm(id_make_model=id_for_delete)
    await delete_make_model(db_helper=db_helper, make_model=form_data)
    return status.HTTP_202_ACCEPTED
