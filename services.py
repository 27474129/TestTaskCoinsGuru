import requests
import config
import redis
from random import randint


class TwitterParsing:
    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
        "Authorization": f"Bearer {config.API_BEARER_TOKEN}"
    }
    proxies = {
        "https": "https://139.162.131.23:8888",
    }

    @staticmethod
    def get_username_from_link(link: str) -> str:
        return link.split("/")[-1]

    def get_user_data(self, user_name: str):
        twitter_id: int
        name: str
        following_count: int
        followers_count: int
        description: str

        data = requests.get(f"https://api.twitter.com/2/users/by/username/elonmusk", \
                            headers=self.headers, proxies=self.proxies, timeout=3).text

        twitter_id = data["data"]["id"]
        name = data["data"]["name"]

    def execute(self):
        self.get_user_data("elonmusk")


def get_task_id() -> int:
    r = redis.Redis(host="redis")
    while True:
        task_id = randint(1, 999999)
        if r.get(task_id) is None:
            return task_id
