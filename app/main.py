from fastapi import FastAPI, Request

from contextlib import asynccontextmanager

from starlette.staticfiles import StaticFiles

from core.models.db_helper import db_helper
from core.models.base import get_db_migration_stmts
from create_fastapi_app import create_app
from routers.api.views import router as api_router
from routers.debug.views import router as debug_router
from routers.frontend.views import router as frontend_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    for stmt in get_db_migration_stmts():
        await db_helper.execute(stmt)
    await db_helper.commit_and_close()
    yield
    # shutdown


app = create_app(create_custom_static_urls=False, lifespan=lifespan)

app.mount("/static", StaticFiles(directory="static"), name="static")


app.include_router(api_router)
app.include_router(debug_router)
app.include_router(frontend_router)
