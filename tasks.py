import redis
import json
from celery import Celery
from services import TwitterParsing
from random import randint


app = Celery("tasks", broker="redis://redis:6379")
app.autodiscover_tasks()


@app.task
def pull_links(task_id, links: dict):
    r = redis.Redis(host="redis")
    result = {}
    for id in links:
        username = TwitterParsing.get_username_from_link(links[id])
        result[id] = {"username": username, "status": "pending"}

    r.set(task_id, json.dumps(result))
