import psycopg2
import config
import logging


logger = logging.getLogger(__name__)


class Postgresql:
    @staticmethod
    def get_connection():
        try:
            return psycopg2.connect(f"dbname={config.DB_NAME} user={config.DB_USERNAME} password={config.DB_PASSWORD} host={config.HOST}")
        except Exception as e:
            logger.error(e)
            return False

    @staticmethod
    def execute_query(connection, request: str) -> list or bool:
        logger.debug(type(connection))
        cursor = connection.cursor()
        try:
            cursor.execute(request)
        except Exception as e:
            logger.error(e)
            return False
        connection.commit()
        try:
            response = cursor.fetchall()
            return response
        except:
            return True

    # метод который открывает конект с бд, выполняет запрос и закрывает конект
    @staticmethod
    def execute_single_query(request: str) -> list or bool:
        try:
            with psycopg2.connect(
                f"dbname={config.DB_NAME} user={config.DB_USERNAME} password={config.DB_PASSWORD} host={config.HOST}"
            ) as connection:
                if connection:
                    with connection.cursor() as cursor:
                        try:
                            cursor.execute(request)
                        except Exception as e:
                            logger.error(e)
                            return False
                        connection.commit()
                        try:
                            response = cursor.fetchall()
                            return response
                        except:
                            return True
        except Exception as e:
            logger.error(e)
            return False
