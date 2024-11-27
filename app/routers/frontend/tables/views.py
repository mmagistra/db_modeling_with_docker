from fastapi import APIRouter

from .cars.views import router as cars_router
from .make_models.views import router as make_models_router
from .orders.views import router as orders_router
from .owners.views import router as owners_router
from .work_types.views import router as work_types_router
from .works_in_order.views import router as works_in_order_router


router = APIRouter(prefix='/table')

router.include_router(cars_router)
router.include_router(make_models_router)
router.include_router(orders_router)
router.include_router(owners_router)
router.include_router(work_types_router)
router.include_router(works_in_order_router)
