from db_manager.abstract_factory import QueryBuilder

class MySQLQueryBuilder(QueryBuilder):
    def build_query_stmt(self, table: str):
        return f'SELECT * FROM {table} LIMIT 10' # MySQL 特定