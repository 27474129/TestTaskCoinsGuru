import logging
from fastapi import FastAPI
from logger_configuration import configure_logger
from modules.users.api import users_router
from config import BASE_API_PREFIX


configure_logger(level="DEBUG")
logger = logging.getLogger(__name__)


app = FastAPI()
app.include_router(users_router)


@app.get(f"{BASE_API_PREFIX}")
async def root():
    return {"success": True, "message": "ROOT PAGE"}
