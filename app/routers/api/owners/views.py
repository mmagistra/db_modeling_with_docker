from typing import Annotated, List

from fastapi import APIRouter, Form
from starlette import status

from core.models.db_helper import db_helper
from routers.api.owners.model import (
    read_all_owners,
    read_owner,
    create_owner,
    update_owner,
    delete_owner
)
from routers.api.owners.schemas import (
    OwnerReadForm,
    OwnerCreateForm,
    Owner,
    OwnerUpdateForm,
    OwnerDeleteForm
)

router = APIRouter(prefix='/owners', tags=['Owners'])


@router.get('/read')
async def handler_read_all_owners():
    data = await read_all_owners(db_helper=db_helper)
    response_forms: List[Owner] = []
    for owner in data:
        response_forms.append(Owner(**owner.model_dump()))
    return data


@router.get('/read/{id_owner}')
async def handler_read_owner_by_id(
        id_owner: int
):
    form_data = OwnerReadForm(id_owner=int(id_owner))
    data = await read_owner(db_helper=db_helper, owner=form_data)
    if data is None:
        return data
    response_form = Owner(**data.model_dump())
    return response_form


@router.post('/create')
async def handler_create_owner(
        form_data: Annotated[OwnerCreateForm, Form()]
):
    await create_owner(db_helper=db_helper, owner=form_data)
    return status.HTTP_201_CREATED


@router.post('/update')
async def handler_update_owner(
        form_data: Annotated[OwnerUpdateForm, Form()]
):
    await update_owner(db_helper=db_helper, owner=form_data)
    return status.HTTP_202_ACCEPTED


@router.post('/delete')
async def handle_delete_owner(
        form_data: Annotated[OwnerDeleteForm, Form()]
):
    await delete_owner(db_helper=db_helper, owner=form_data)
    return status.HTTP_202_ACCEPTED
