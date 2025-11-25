# 笨拙的方法
config = {}
if 'host' not in config:
    config['host'] = 'localhost'
if 'port' not in config:
    config['port'] = 8080
if 'database_url' not in config:
    config['database_url'] = 'sqlite:///:memory:'
if 'timeout' not in config:
    config['timeout'] = 30