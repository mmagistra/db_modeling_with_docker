from typing import Annotated, Optional

from fastapi import Form
from pydantic import BaseModel


class CarCreateForm(BaseModel):
    fk_owner: int
    fk_make_model: int
    release_year: int
    car_number: str


class CarDeleteForm(BaseModel):
    id_car: int


class CarReadForm(CarDeleteForm):
    pass


class CarUpdateForm(BaseModel):
    id_car: int
    fk_owner: Optional[int] = None
    fk_make_model: Optional[int] = None
    release_year: Optional[int] = None
    car_number: Optional[str] = None


class Car(BaseModel):
    id_car: int
    fk_owner: int
    fk_make_model: int
    release_year: int
    car_number: str
