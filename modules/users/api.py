import logging
from modules.routers import users_router
from modules.users.schemas import UserCreationModel
from .repository import UserModelRepository


logger = logging.getLogger(__name__)


@users_router.post("/")
async def create_user(user_data: UserCreationModel):
    UserModelRepository.add_user(user_data)
    return {"success": True, "new_user": user_data}


@users_router.put("/")
async def update_user(user_da):
    pass
