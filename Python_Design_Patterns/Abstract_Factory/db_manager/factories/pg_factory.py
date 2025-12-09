from db_manager.abstract_factory import DBFactory, DBConnector, QueryBuilder, TransactionManager
from db_manager.postgresql_db.connector import PostgreSQLConnector
from db_manager.postgresql_db.query_builder import PostgreSQLQueryBuilder
from db_manager.postgresql_db.tx_manager import PostgreSQLTransactionManager

class PostgreSQLFactory(DBFactory):
    def create_connector(self) -> DBConnector:
        return PostgreSQLConnector()
    
    def create_query_builder(self) -> QueryBuilder:
        return PostgreSQLQueryBuilder()
    
    def create_transaction_manager(self) -> TransactionManager:
        return PostgreSQLTransactionManager()