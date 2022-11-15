import os
from dotenv import load_dotenv


load_dotenv()


ROOT_DIR = "/sources"
DB_NAME = os.getenv("DB_NAME")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
HOST = os.getenv("HOST")
BASE_API_PREFIX = os.getenv("BASE_API_PREFIX")
