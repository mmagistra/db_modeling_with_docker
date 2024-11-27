import os

from core.models.base import get_db_migration_stmts, get_default_data_insert_stmts
from core.models.db_helper import DatabaseHelper
from routers.api.cars.schemas import CarCreateForm, Car, CarUpdateForm, CarDeleteForm, CarReadForm
from routers.api.cars.views import (
    handler_read_all_cars,
    handler_create_car,
    handler_update_car,
    handler_read_car_by_id,
    handle_delete_car
)


class TestModelsViews:
    async def setup(self):
        db_path = """sqlite:./test_db.sqlite3"""
        self.db_helper = DatabaseHelper(db_path, echo=False)
        for stmt in get_db_migration_stmts():
            await self.db_helper.execute(stmt)
        await self.db_helper.commit()

        for stmt in get_default_data_insert_stmts():
            await self.db_helper.execute(stmt)
        await self.db_helper.commit()

    async def teardown(self):
        os.remove('./test_db.sqlite3')

    async def test_cars(
            self,
            car_for_checks: Car,
            updated_car_for_checks: Car,
            create_car: CarCreateForm,
            update_car: CarUpdateForm,
            delete_car: CarDeleteForm,
            read_exist_car: CarReadForm,
            read_none_exist_car: CarReadForm,
    ):
        # read all cars
        all_cars = await handler_read_all_cars()
        assert len(all_cars) == 5

        # add one car
        await handler_create_car(create_car)
        all_cars = await handler_read_all_cars()
        assert len(all_cars) == 6

        # take new car
        exist_car = await handler_read_car_by_id(read_exist_car)
        assert exist_car == car_for_checks

        # update car and check for updates
        await handler_update_car(update_car)
        exist_car = await handler_read_car_by_id(read_exist_car)
        assert exist_car == updated_car_for_checks

        # delete car and check it
        await handle_delete_car(delete_car)
        all_cars = await handler_read_all_cars()
        assert len(all_cars) == 5

        none_exist_car = await handler_read_car_by_id(read_none_exist_car)
        assert none_exist_car is None
