from pytest import fixture

from routers.api.cars.schemas import Car, CarCreateForm, CarUpdateForm, CarDeleteForm, CarReadForm


@fixture
def car_for_checks():
    car = Car(
        id_car=6,
        fk_owner=1,
        fk_make_model=1,
        release_year=1900,
        car_number='A123BC',
    )
    return car


@fixture
def updated_car_for_checks():
    car = Car(
        id_car=6,
        fk_owner=1,
        fk_make_model=1,
        release_year=2000,
        car_number='C321BA',
    )
    return car


@fixture
def create_car():
    new_car = CarCreateForm(
        fk_owner=1,
        fk_make_model=1,
        release_year=1900,
        car_number='A123BC'
    )
    return new_car


@fixture
def update_car():
    new_car = CarUpdateForm(
        id_car=6,
        release_year=2000,
        car_number='C321BA'
    )
    return new_car


@fixture
def delete_car():
    new_car = CarDeleteForm(
        id_car=6
    )
    return new_car


@fixture
def read_exist_car():
    new_car = CarReadForm(
        id_car=6
    )
    return new_car


@fixture
def read_none_exist_car():
    new_car = CarReadForm(
        id_car=7
    )
    return new_car
