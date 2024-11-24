from typing import Optional

from pydantic import BaseModel


class WorkInOrderCreateForm(BaseModel):
    fk_order: int
    fk_work_type: int
    work_number: int
    count: int
    amount: float


class WorkInOrderDeleteForm(BaseModel):
    id_work_in_order: int


class WorkInOrderReadForm(WorkInOrderDeleteForm):
    pass


class WorkInOrderUpdateForm(BaseModel):
    id_work_in_order: int
    fk_order: Optional[int] = None
    fk_work_type: Optional[int] = None
    work_number: Optional[int] = None
    count: Optional[int] = None
    amount: Optional[float] = None


class WorkInOrder(BaseModel):
    id_work_in_order: int
    fk_order: int
    fk_work_type: int
    work_number: int
    count: int
    amount: float

