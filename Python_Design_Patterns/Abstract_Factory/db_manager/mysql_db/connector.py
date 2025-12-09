import mysql.connector
from mysql.connector import pooling
from mysql.connector.errors import Error as MySQLError
import logging

from db_manager.abstract_factory import DBConnector

logging.basicConfig(level=logging.ERROR)

class MySQLConnector(DBConnector):
    def __init__(self):
        try:
            self.pool = pooling.MySQLConnectionPool(
                pool_name='mypool',
                pool_size=5, # 连接池大小，可配置
                user='user',
                password='pass',
                host='localhost',
                database='db'
            )
        except MySQLError as e:
            logging.error(f'Failed  to create MySQL connection pool: {e}')
            raise

    def connect(self):
        try:
            return self.pool.get_connection()
        except MySQLError as e:
            logging.error(f'Failed to get connection from pool: {e}')
            raise

    def close(self, connection):
        if connection:
            connection.close()