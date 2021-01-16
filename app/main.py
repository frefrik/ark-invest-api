from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from fastapi.middleware.cors import CORSMiddleware
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from .database import engine
from .models import Base
from .routers import v1
from .tasks import check_for_updates, update_trades, update_holdings
from .config import (
    OPENAPI_API_VERSION, OPENAPI_CONTACT, OPENAPI_DESCRIPTION,
    OPENAPI_EXTERNALDOCS_DESC, OPENAPI_EXTERNALDOCS_URL, OPENAPI_HOST,
    OPENAPI_SERVER_BASEPATH, OPENAPI_SERVER_URL, OPENAPI_TITLE,
    UPDATE_INTERVAL_HOLDINGS, UPDATE_INTERVAL_TRADES
)

Base.metadata.create_all(bind=engine)

scheduler = AsyncIOScheduler()
scheduler.start()

APP = FastAPI(
    docs_url="/api",
    redoc_url="/api/docs",
    on_startup=[check_for_updates],
    openapi_url="/api/openapi.json"
)


def custom_openapi():
    if APP.openapi_schema:
        return APP.openapi_schema

    openapi_schema = get_openapi(
        title=OPENAPI_TITLE,
        version=OPENAPI_API_VERSION,
        description=OPENAPI_DESCRIPTION,
        routes=APP.routes,
    )

    openapi_schema["info"]["contact"] = {
        "email": OPENAPI_CONTACT
    }

    openapi_schema["host"] = OPENAPI_HOST
    openapi_schema["servers"] = [
        {
            "url": OPENAPI_SERVER_URL,
            "basePath": OPENAPI_SERVER_BASEPATH
        }
    ]

    openapi_schema["externalDocs"] = {
        "description": OPENAPI_EXTERNALDOCS_DESC,
        "url": OPENAPI_EXTERNALDOCS_URL
    }

    APP.openapi_schema = openapi_schema

    return APP.openapi_schema


APP.openapi = custom_openapi

APP.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

scheduler.add_job(
    update_trades,
    'interval',
    seconds=UPDATE_INTERVAL_TRADES
)

scheduler.add_job(
    update_holdings,
    'interval',
    seconds=UPDATE_INTERVAL_HOLDINGS
)


APP.include_router(v1, prefix="/api/v1")
