from fastapi import FastAPI, Request

from contextlib import asynccontextmanager

from starlette.staticfiles import StaticFiles

from core.models.db_helper import db_helper
from core.models.base import Base
from create_fastapi_app import create_app


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.create_all_tables)
    yield
    # shutdown


app = create_app(create_custom_static_urls=False, lifespan=lifespan)

app.mount("/static", StaticFiles(directory="static"), name="static")

# app.include_router(about_router)


@app.get("/hello/", tags=['Test'])
def hello_world():
    return {"message": "Hello World"}
