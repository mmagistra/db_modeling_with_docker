from enum import Enum
from typing import List, Any, Optional

from pydantic import BaseModel


class AvailableFieldTypes(str, Enum):
    text = 'text'
    string = 'string'
    integer = 'integer'
    id = 'id'
    foreign_key = 'foreign_key'
    date = 'date'
    float = 'float'


class Choice(BaseModel):
    id: int
    hint: str
    selected: Optional[bool] = False


class Field(BaseModel):
    name: str
    field_type: AvailableFieldTypes
    enable: Optional[bool] = True
    choices: Optional[List[Choice]] = None
    value: Optional[Any] = None
