from routers.api.cars.schemas import CarUpdateForm
from routers.frontend.tables.schemas import Field

a = Field(name='release_year', field_type='integer')
print(a)
