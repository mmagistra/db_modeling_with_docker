from fastapi import APIRouter

from .tables.views import router as tables_router
from routers.frontend.accountings.views import router as accounting_router

router = APIRouter(prefix='', tags=['Frontend'])

router.include_router(tables_router)
router.include_router(accounting_router)
