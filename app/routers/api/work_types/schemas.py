from typing import Optional

from pydantic import BaseModel


class WorkTypeCreateForm(BaseModel):
    name: str
    price: float


class WorkTypeDeleteForm(BaseModel):
    id_work_type: int


class WorkTypeReadForm(WorkTypeDeleteForm):
    pass


class WorkTypeUpdateForm(BaseModel):
    id_work_type: int
    name: Optional[str] = None
    price: Optional[float] = None


class WorkType(BaseModel):
    id_work_type: int
    name: str
    price: float

