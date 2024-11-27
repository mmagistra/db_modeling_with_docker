from typing import List

from routers.api.cars.schemas import Car
from routers.api.make_models.model import read_make_models_human_identify_fields
from routers.api.owners.model import read_owners_human_identify_fields
from routers.frontend.tables.schemas import Choice, Field


async def get_form_fields(
        db_helper,
        ID_FIELD_NAME: str = ''
):
    owners_hints = await read_owners_human_identify_fields(db_helper)
    owners_choices = []
    for hint in owners_hints:
        owners_choices += [
            Choice(
                id=hint['id_owner'],
                hint=f'{hint['id_owner']}. {hint['name']}'
            )
        ]

    make_models_hints = await read_make_models_human_identify_fields(db_helper)
    make_models_choices = []
    for hint in make_models_hints:
        make_models_choices += [
            Choice(
                id=hint['id_make_model'],
                hint=f'{hint['id_make_model']}. {hint['make_model']}'
            )
        ]

    FORM_FIELDS: List[Field] = [
        Field(name='fk_owner', field_type='foreign_key', choices=owners_choices),
        Field(name='fk_make_model', field_type='foreign_key', choices=make_models_choices),
        Field(name='release_year', field_type='integer'),
        Field(name='car_number', field_type='string')
    ]
    if ID_FIELD_NAME != '':
        FORM_FIELDS = [Field(name=ID_FIELD_NAME, field_type='id', enable=False)] + FORM_FIELDS
    return FORM_FIELDS
