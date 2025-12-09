from db_manager.abstract_factory import QueryBuilder

class PostgreSQLQueryBuilder(QueryBuilder):
    def build_query_stmt(self, table):
        return f'SELECT * FROM {table} LIMIT 10'  # 可扩展差异，如 LIKE 