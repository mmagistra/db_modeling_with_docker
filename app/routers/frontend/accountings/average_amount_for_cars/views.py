from typing import List

from fastapi import APIRouter, Request

from core.models.db_helper import db_helper
from routers.frontend.accountings.average_amount_for_cars.schemas import (
    IS_PAGE_ACTIVE_CONDITION_NAME,
    NAME_PLURAL,
    RU_NAME_PLURAL,
    AvgAmountForCars
)
from routers.frontend.accountings.models import read_fields_by_statement_and_convert_to_class_list
from routers.frontend.post_processes import post_process_handler

router = APIRouter(prefix='/avg_amount_for_cars')


@router.get('/calculate')
async def calculate(
        request: Request,
):
    STMT_FOR_CALCULATE = """
    SELECT 
        cars.id_car,
        cars.car_number,
        AVG(works_in_order.amount) AS avg_order_amount
    FROM 
        cars
    JOIN 
        orders ON cars.id_car = orders.fk_car
    JOIN 
        works_in_order ON orders.id_order = works_in_order.fk_order
    GROUP BY 
        cars.id_car, cars.car_number
    ORDER BY
        cars.id_car;
    """
    data: List[AvgAmountForCars] = await read_fields_by_statement_and_convert_to_class_list(
        db_helper,
        stmt=STMT_FOR_CALCULATE,
        ClassForConvert=AvgAmountForCars,
    )

    link_fields = {}
    data: List[dict] = [i.model_dump() for i in data]

    context = {
        IS_PAGE_ACTIVE_CONDITION_NAME: True,
        'model': {
            'name_plural': NAME_PLURAL,
            'ru_name_plural': RU_NAME_PLURAL,
            'data': data,
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
