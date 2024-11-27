from typing import List

from fastapi import APIRouter, Request

from core.models.db_helper import db_helper
from routers.frontend.accountings.total_price_by_work_types.schemas import (
    IS_PAGE_ACTIVE_CONDITION_NAME,
    NAME_PLURAL,
    RU_NAME_PLURAL,
    TotalPriceByWorkTypes
)
from routers.frontend.accountings.models import read_fields_by_statement_and_convert_to_class_list
from routers.frontend.accountings.total_price_by_work_types.schemas import TotalPriceByWorkTypes
from routers.frontend.post_processes import post_process_handler

router = APIRouter(prefix='/total_price_by_work_type')


@router.get('/calculate')
async def calculate(
        request: Request,
):
    STMT_FOR_CALCULATE = """
    SELECT 
        work_types.id_work_type,
        work_types.name,
        COUNT(works_in_order.id_work_in_order) AS carried_out_times,
        SUM(works_in_order.amount) AS total_amount
    FROM 
        work_types
    LEFT JOIN 
        works_in_order ON work_types.id_work_type = works_in_order.fk_work_type
    GROUP BY 
        work_types.id_work_type, work_types.name
    ORDER BY
        work_types.id_work_type;

    """
    data: List[TotalPriceByWorkTypes] = await read_fields_by_statement_and_convert_to_class_list(
        db_helper,
        stmt=STMT_FOR_CALCULATE,
        ClassForConvert=TotalPriceByWorkTypes,
    )

    link_fields = {}
    response_data: List[dict] = []
    for instance in data:
        instance_data = instance.model_dump()
        if instance_data['total_amount'] is None:
            instance_data['total_amount'] = float(0)
        response_data.append(instance_data)

    context = {
        IS_PAGE_ACTIVE_CONDITION_NAME: True,
        'model': {
            'name_plural': NAME_PLURAL,
            'ru_name_plural': RU_NAME_PLURAL,
            'data': response_data,
            'fk_fields': link_fields
        }
    }

    return await post_process_handler(
        request,
        context,
        level=3,
        template_name='accounting_read.html',
        placement='accounting',
    )
