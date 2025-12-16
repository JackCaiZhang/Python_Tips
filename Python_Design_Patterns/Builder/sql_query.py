class SQLQuery:
    """
    产品角色：最终生成的 SQL 对象
    """
    def __init__(self, sql: str, params: list):
        self.sql = sql
        self.params = params

    def __str__(self):
        return f"SQL: {self.sql} | Params: {self.params}"