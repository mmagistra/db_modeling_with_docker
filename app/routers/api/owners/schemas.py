from typing import Optional

from pydantic import BaseModel


class OwnerCreateForm(BaseModel):
    name: str
    phone_number: int


class OwnerDeleteForm(BaseModel):
    id_owner: int


class OwnerReadForm(OwnerDeleteForm):
    pass


class OwnerUpdateForm(BaseModel):
    id_owner: int
    name: Optional[str] = None
    phone_number: Optional[int] = None


class Owner(BaseModel):
    id_owner: int
    name: str
    phone_number: int

