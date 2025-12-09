from db_manager.abstract_factory import DBFactory, DBConnector, QueryBuilder, TransactionManager
from db_manager.mysql_db.connector import MySQLConnector
from db_manager.mysql_db.query_builder import MySQLQueryBuilder
from db_manager.mysql_db.tx_manager import MySQLTransactionManager

class MySQLFactory(DBFactory):
    def create_connector(self) -> DBConnector:
        return MySQLConnector()
    
    def create_query_builder(self) -> QueryBuilder:
        return MySQLQueryBuilder()
    
    def create_transaction_manager(self) -> TransactionManager:
        return MySQLTransactionManager()