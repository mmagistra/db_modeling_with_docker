from pydantic import BaseModel

IS_PAGE_ACTIVE_CONDITION_NAME = 'is_average_amount_for_cars_active'
NAME_PLURAL = 'Average amount of order price for every car'
RU_NAME_PLURAL = 'Средняя сумма заказа для каждой машины'


class AvgAmountForCars(BaseModel):
    id_car: int
    car_number: str
    avg_order_amount: float | None
