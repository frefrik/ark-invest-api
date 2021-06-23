from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.openapi.utils import get_openapi
from fastapi.middleware.cors import CORSMiddleware
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from .database import engine
from .models import Base
from .routers import v1
from .tasks import update_etf_news, update_trades, update_holdings
from .config import (
    OPENAPI_API_VERSION,
    OPENAPI_CONTACT,
    OPENAPI_DESCRIPTION,
    OPENAPI_EXTERNALDOCS_DESC,
    OPENAPI_EXTERNALDOCS_URL,
    OPENAPI_HOST,
    OPENAPI_SERVER_BASEPATH,
    OPENAPI_SERVER_URL,
    OPENAPI_TITLE,
    UPDATE_INTERVAL_TRADES,
)

Base.metadata.create_all(bind=engine)

scheduler = AsyncIOScheduler()
scheduler.start()

APP = FastAPI()


@APP.get("/", response_class=HTMLResponse)
async def read_items():
    with open("app/static/index.html") as f:
        html_content = f.read()

    return HTMLResponse(content=html_content, status_code=200)


api = FastAPI(
    docs_url="/",
    redoc_url="/docs",
    on_shutdown=[scheduler.shutdown],
    openapi_url="/openapi.json",
)


def custom_openapi():
    if api.openapi_schema:
        return api.openapi_schema

    openapi_schema = get_openapi(
        title=OPENAPI_TITLE,
        version=OPENAPI_API_VERSION,
        description=OPENAPI_DESCRIPTION,
        routes=api.routes,
    )

    openapi_schema["info"]["contact"] = {"email": OPENAPI_CONTACT}

    openapi_schema["host"] = OPENAPI_HOST
    openapi_schema["servers"] = [
        {"url": OPENAPI_SERVER_URL, "basePath": OPENAPI_SERVER_BASEPATH}
    ]

    openapi_schema["externalDocs"] = {
        "description": OPENAPI_EXTERNALDOCS_DESC,
        "url": OPENAPI_EXTERNALDOCS_URL,
    }

    api.openapi_schema = openapi_schema

    return api.openapi_schema


api.openapi = custom_openapi

api.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

scheduler.add_job(
    update_trades,
    "cron",
    day_of_week="*",
    hour="*",
    minute=f"*/{UPDATE_INTERVAL_TRADES}",
)

scheduler.add_job(
    update_holdings,
    "cron",
    day_of_week="*",
    hour="*",
    minute="0",
)

scheduler.add_job(
    update_etf_news,
    "cron",
    hour="*",
    minute="*/10",
)

api.include_router(v1, prefix="/v1")
APP.mount("/api", api)
APP.mount("/static", StaticFiles(directory="app/static", html=True), name="static")