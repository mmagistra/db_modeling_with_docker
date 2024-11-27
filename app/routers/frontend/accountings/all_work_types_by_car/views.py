from typing import List

from fastapi import APIRouter, Request

from core.models.db_helper import db_helper
from routers.frontend.accountings.all_work_types_by_car.schemas import (
    IS_PAGE_ACTIVE_CONDITION_NAME,
    NAME_PLURAL,
    RU_NAME_PLURAL,
    AllWorkTypesByCar
)
from routers.frontend.accountings.models import read_fields_by_statement_and_convert_to_class_list
from routers.frontend.post_processes import post_process_handler

router = APIRouter(prefix='/all_work_types_by_car')


@router.get('/calculate')
async def calculate(
        request: Request,
):
    STMT_FOR_CALCULATE = """
    SELECT 
        cars.id_car,
        cars.car_number,
        COUNT(works_in_order.id_work_in_order) AS work_count,
        SUM(works_in_order.amount) AS total_work_amount
    FROM 
        cars
    LEFT JOIN 
        orders ON cars.id_car = orders.fk_car
    LEFT JOIN 
        works_in_order ON orders.id_order = works_in_order.fk_order
    GROUP BY 
        cars.id_car, cars.car_number
    ORDER BY
        cars.id_car;
    """
    data: List[AllWorkTypesByCar] = await read_fields_by_statement_and_convert_to_class_list(
        db_helper,
        stmt=STMT_FOR_CALCULATE,
        ClassForConvert=AllWorkTypesByCar,
    )

    link_fields = {}
    response_data: List[dict] = []
    for instance in data:
        instance_data = instance.model_dump()
        if instance_data['total_work_amount'] is None:
            instance_data['total_work_amount'] = float(0)
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
