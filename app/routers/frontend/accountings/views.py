from fastapi import APIRouter, Request

from routers.frontend.accountings.average_amount_for_cars.views import router as average_amount_for_cars_router
from routers.frontend.accountings.all_work_types_by_car.views import router as all_work_types_by_car_router
from routers.frontend.accountings.total_price_by_work_types.views import router as total_price_by_work_types_router


router = APIRouter(prefix='/accounting')

router.include_router(average_amount_for_cars_router)
router.include_router(all_work_types_by_car_router)
router.include_router(total_price_by_work_types_router)
