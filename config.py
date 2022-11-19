import os
from dotenv import load_dotenv


load_dotenv()


ROOT_DIR = "/sources"
DB_NAME = os.getenv("DB_NAME")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
HOST = os.getenv("HOST")
BASE_API_PREFIX = os.getenv("BASE_API_PREFIX")
ACCESS_TOKEN=os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")
API_KEY = os.getenv("API_KEY")
API_SECRET_KEY = os.getenv("API_SECRET_KEY")
API_BEARER_TOKEN = os.getenv("API_BEARER_TOKEN")
PROXIES = os.getenv("PROXIES")
