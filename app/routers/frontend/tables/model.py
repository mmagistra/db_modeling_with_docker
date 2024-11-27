from typing import List

from routers.frontend.tables.schemas import Field


async def set_values_for_form_fields(
        data,
        fields: List[Field],
        enable_fields: bool = True
):
    data: dict = data.model_dump()
    for field in fields:
        field.enable = enable_fields
        if field.field_type == 'id':
            field.enable = False

        if field.field_type == 'foreign_key':
            for choice in field.choices:
                if choice.id == data[field.name]:
                    choice.selected = True
        else:
            field.value = data[field.name]
    return fields
