from typing import List

from routers.api.cars.schemas import Car
from routers.api.make_models.model import read_make_models_human_identify_fields
from routers.api.orders.model import read_orders_human_identify_fields
from routers.api.owners.model import read_owners_human_identify_fields
from routers.frontend.tables.schemas import Choice, Field


async def get_form_fields(
        db_helper,
        ID_FIELD_NAME: str = ''
):
    orders_hints = await read_orders_human_identify_fields(db_helper)
    orders_choices = []
    for hint in orders_hints:
        orders_choices += [
            Choice(
                id=hint['id_order'],
                hint=f'{hint['id_order']}. {hint['order_number']}'
            )
        ]

    FORM_FIELDS: List[Field] = [
        Field(name='date', field_type='date'),
        Field(name='fk_order', field_type='foreign_key', choices=orders_choices),
    ]
    if ID_FIELD_NAME != '':
        FORM_FIELDS = [Field(name=ID_FIELD_NAME, field_type='id', enable=False)] + FORM_FIELDS
    return FORM_FIELDS
