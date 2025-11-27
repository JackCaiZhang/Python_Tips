# service_a.py
import db_pool

def run():
    pool_a = db_pool.get_connection_pool()
    print(f'A 模块：{pool_a} (ID: {id(pool_a)})')

    # A 模块修改了配置
    db_pool.set_pool_size(20)

if __name__ == '__main__':
    run()