from sql_query import SQLQuery

class SQLQueryBuilder:
    """
    建造者角色：负责分步构建 SQL
    """
    def __init__(self):
        # 内部暂存构建过程中的状态
        self._table = ""
        self._columns = []
        self._conditions = []   # 存储 where 条件
        self._params = []       # 存储参数化查询的值（防止 SQL 注入）
        self._order_by = ""
        self._limit = None

    def select(self, *columns):
        """步骤1：选择列"""
        self._columns.extend(columns)
        return self # 关键：返回 self 以便链式调用
    
    def from_table(self, table: str):
        """步骤2：选择表"""
        self._table = table
        return self
    
    def where(self, condition: str, *params):
        """
        步骤3：添加 where 条件
        支持多次调用 where，自动 AND 连接
        """
        self._conditions.append(condition)
        self._params.extend(params)
        return self
    
    def order_by(self, order: str):
        """步骤4：排序"""
        self._order_by = order
        return self
    
    def limit(self, limit: int):
        """步骤5：限制数量"""
        self._limit = limit
        return self
    
    def build(self) -> SQLQuery:
        """
        最后一步：构建产品
        在这里进行复杂的组装逻辑和校验
        """
        # 1. 校验必填项
        if not self._table:
            raise ValueError("Table is required! Please call 'from_table()' first.")
        
        # 2. 组装 SQL 字符串
        columns_str = ', '.join(self._columns) if self._columns else '*'
        sql_parts = [f"SELECT {columns_str} FROM {self._table}"]

        # 3. 处理 where 子句
        if self._conditions:
            where_clause = ' AND '.join(self._conditions)
            sql_parts.append(f"WHERE {where_clause}")

        # 4. 处理排序
        if self._order_by:
            sql_parts.append(f"ORDER BY {self._order_by}")

        # 5. 处理 Limit
        if self._limit is not None:
            sql_parts.append(f"LIMIT {self._limit}")

        # 6. 返回最终的产品对象
        return SQLQuery(' '.join(sql_parts), self._params)