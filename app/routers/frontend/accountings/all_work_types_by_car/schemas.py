from pydantic import BaseModel

IS_PAGE_ACTIVE_CONDITION_NAME = 'is_all_work_types_by_car'
NAME_PLURAL = 'All work types by car'
RU_NAME_PLURAL = 'Все типы работ проведенные для машины'


class AllWorkTypesByCar(BaseModel):
    id_car: int
    car_number: str
    work_count: int
    total_work_amount: float | None
