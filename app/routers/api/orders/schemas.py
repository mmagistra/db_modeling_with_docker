from typing import Optional
from datetime import date as date_type

from pydantic import BaseModel


class OrderCreateForm(BaseModel):
    date: date_type
    fk_car: int

    def model_dump(self, **kwargs):
        data = super().model_dump(**kwargs)
        data['date'] = self.date.strftime('%Y-%m-%d')
        return data


class OrderDeleteForm(BaseModel):
    id_order: int


class OrderReadForm(OrderDeleteForm):
    pass


class OrderUpdateForm(BaseModel):
    id_order: int
    date: Optional[date_type] = None
    fk_car: Optional[int] = None


class Order(BaseModel):
    id_order: int
    date: date_type
    fk_car: int

