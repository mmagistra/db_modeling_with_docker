from fastapi import APIRouter

from .tables.views import router as tables_router

router = APIRouter(prefix='', tags=['Frontend'])

router.include_router(tables_router)
