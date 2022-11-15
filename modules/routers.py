from fastapi import APIRouter
from config import BASE_API_PREFIX


users_router = APIRouter(prefix=f"{BASE_API_PREFIX}/users")
