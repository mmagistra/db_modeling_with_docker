from typing import List

from routers.api.cars.schemas import Car
from routers.api.make_models.model import read_make_models_human_identify_fields
from routers.api.owners.model import read_owners_human_identify_fields
from routers.frontend.tables.schemas import Choice, Field


async def get_form_fields(
        db_helper,
        ID_FIELD_NAME: str = ''
):
    FORM_FIELDS: List[Field] = [
        Field(name='make_model', field_type='string')
    ]

    if ID_FIELD_NAME != '':
        FORM_FIELDS = [Field(name=ID_FIELD_NAME, field_type='id', enable=False)] + FORM_FIELDS
    return FORM_FIELDS
