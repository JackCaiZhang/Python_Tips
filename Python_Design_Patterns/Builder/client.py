from sql_query_builder import SQLQueryBuilder

def main():
    # 场景：我们需要查询“活跃用户”，年龄大于18，按注册时间排序，取前10个
    builder = SQLQueryBuilder()
    
    query = (
        builder
        .select('user_id', 'username', 'email')
        .from_table('users')
        .where('status = ?', 'active')  # 参数化查询
        .where('age > ?', 18)           # 再次添加条件，自动 AND
        .order_by('created_at DESC')
        .limit(10)
        .build()
    )
    
    print(query)

    # 模拟执行
    # db.execute(query.sql, query.params)

if __name__ == "__main__":
    main()