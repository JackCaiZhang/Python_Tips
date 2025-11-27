# service_b.py
import db_pool

def run():
    pool_b = db_pool.get_connection_pool()
    print(f'B 模块：{pool_b} (ID: {id(pool_b)})')

if __name__ == '__main__':
    run()