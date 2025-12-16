from sql_query_builder import SQLQueryBuilder

class QueryDirector:
    """
    指挥者：封装常用的查询构建流程
    """
    def __init__(self, builder: SQLQueryBuilder):
        self.builder = builder

    def construct_recent_active_users(self):
        """
        构建一个标准的“最近活跃用户”查询
        """
        return (
            self.builder
            .select('user_id', 'username', 'email')
            .from_table('users')
            .where('status = ?', 'active')
            .order_by('last_login DESC')
            .limit(5)
            .build()
        )
    
# 使用指挥者
director = QueryDirector(SQLQueryBuilder())
standard_query = director.construct_recent_active_users()
print(f'标准查询：{standard_query}')