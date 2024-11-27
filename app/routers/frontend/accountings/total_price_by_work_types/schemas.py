from pydantic import BaseModel

IS_PAGE_ACTIVE_CONDITION_NAME = 'is_total_price_by_work_type'
NAME_PLURAL = 'Total price by work types'
RU_NAME_PLURAL = 'Общая стоимость проведенных работ по типу работы'


class TotalPriceByWorkTypes(BaseModel):
    id_work_type: int
    name: str
    carried_out_times: int
    total_amount: float | None
