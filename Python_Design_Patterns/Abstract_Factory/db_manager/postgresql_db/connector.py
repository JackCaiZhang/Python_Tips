import psycopg2
from psycopg2 import pool, OperationalError
import logging

from db_manager.abstract_factory import DBConnector

logging.basicConfig(level=logging.ERROR)

class PostgreSQLConnector(DBConnector):
    def __init__(self):
        try:
            self.pool = pool.ThreadedConnectionPool(
                minconn=1,
                maxconn=5,  # 连接池大小
                dsn="db_nam='db' user='user' host='localhost' password='pass'"
            )
        except OperationalError as e:
            logging.error(f'Failed to create PostgreSQL connection pool: {e}')
            raise

    def connect(self):
        try:
            return self.pool.getconn()
        except OperationalError as e:
            logging.error(f'Failed to get connection from pool: {e}')
            raise

    def close(self, connection):
        if connection:
            self.pool.putconn(connection)