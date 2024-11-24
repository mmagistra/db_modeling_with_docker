from typing import Optional

from pydantic import BaseModel


class MakeModelCreateForm(BaseModel):
    make_model: str


class MakeModelDeleteForm(BaseModel):
    id_make_model: int


class MakeModelReadForm(MakeModelDeleteForm):
    pass


class MakeModelUpdateForm(BaseModel):
    id_make_model: int
    make_model: Optional[str] = None


class MakeModel(BaseModel):
    id_make_model: int
    make_model: str

