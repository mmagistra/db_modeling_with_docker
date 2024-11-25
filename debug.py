import psycopg
import pprint

from routers.api.make_models.schemas import MakeModel

a = MakeModel().model_dump()
print(a[:-2])
