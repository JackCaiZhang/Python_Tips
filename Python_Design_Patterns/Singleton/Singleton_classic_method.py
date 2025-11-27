import threading

class SingletonDatabase:
    _instance = None
    _lock = threading.Lock()  # 引入线程锁，保证并发安全

    def __new__(cls, *args, **kwargs):
        # 核心：检查实例是否存在
        if cls._instance is None:
            # 如果不存在，加锁
            with cls._lock:
                # 再次检查（双重检查锁定）
                # 为什么？因为可能多个线程同时在等锁
                # 第一个线程创建后，后续线程应直接跳过
                if cls._instance is None:
                    # 调用父类的 __new__ 来真正创建实例
                    cls._instance = super().__new__(cls)
                    cls._instance._initialized = False
        return cls._instance
    
    def __init__(self, db_name):
        # __init__ 每次都会被调用，所以我们用一个标志位
        if getattr(self, '_initialized', False):
            return
        
        print(f'初始化数据库连接... {db_name}')
        self.db_name = db_name
        self._initialized = True

# --- 验证 ---
db1 = SingletonDatabase('MySQL_Pool')
print(f'db1 ID: {id(db1)}, Name: {db1.db_name}')

# 尽管我们尝试用不同的参数再次“创建”
db2 = SingletonDatabase('PostgreSQL_Pool')
print(f'db2 ID: {id(db2)}, Name: {db2.db_name}')

print(f'db1 和 db2 是同一个实例吗？{id(db1) == id(db2)}')