import logging
import redis
import config
import json
from fastapi import FastAPI
from typing import List
from services import TwitterParsing
from tasks import pull_links
from services import get_task_id


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


app = FastAPI()


@app.post(f"{config.BASE_API_PREFIX}/users")
def add_users(links: List[str]):
    task_id = get_task_id()

    result = dict()

    id = 1
    for link in links:
        result[id] = link
        id += 1

    pull_links.delay(task_id, result)

    return {"success": True, "links": result, "task_id": task_id}


@app.get(f"{config.BASE_API_PREFIX}/users/status" + "/{task_id}" + "/{link_id}")
def get_link_status(task_id: int, link_id: int):
    r = redis.Redis(host="redis")
    links = json.loads(r.get(task_id))
    result = links[str(link_id)]
    return {"success": True, "link_status": {"username": result["username"], "status": result["status"]}}
