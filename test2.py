# 优雅的方法
class SmartConfig(dict):
    def __missing__(self, key):
        defaults = {
            'host': 'localhost',
            'port': 8080,
            'database_url': 'sqlite:///:memory:',
            'timeout': 30
        }
        return defaults.get(key, None)
    
config = SmartConfig()
# 现在可以直接访问配置项，即使它们未被显式设置
host = config['host']
port = config['port']
database_url = config['database_url']
timeout = config['timeout']
print(f'Host: {host}')
print(f'Port: {port}')
print(f'Database URL: {database_url}')