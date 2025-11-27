# db_pool.py
# 这是一个模块，它本身就是单例

print('--- 模块被加载，数据库连接池正在初始化... ---')

_connections = {'db_name': 'MySQL_Main_Pool', 'size': 10}

def get_connection_pool():
    """获取全局唯一的连接池"""
    return _connections

def set_pool_size(size):
    """修改连接池配置"""
    _connections['size'] = size

# ... 其他数据库操作