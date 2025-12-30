import copy
import time
import datetime

class Dashboard:
    def __init__(self, name, filters=None):
        self.name = name
        self.filters = filters or []
        self.created_at = datetime.datetime.now()
        # 模拟昂贵的初始化过程
        print(f'[{name}] 正在连接数据库并加载底座数据（模拟耗时）...')
        time.sleep(2)  # 模拟耗时操作
        self.base_data = [1, 2, 3, 4, 5]  # 假设这是几百万条数据

    def show(self):
        print(f'报表： {self.name} | 筛选条件： {self.filters} | 数据地址：{id(self.base_data)}')

# --- 场景演示 ---

# 1. 创建原型（Prototype）
print('--- 1. 创建母版 ---')
start = time.time()
prototype_dash = Dashboard('全公司总览', filters=['全部'])
print(f'母版创建耗时：{time.time() - start:.2f} s\n')

# 2. 克隆并修改
print('--- 2. 快速克隆子报表 ---')
start = time.time()

# 使用 deepcopy（深拷贝）进行克隆
dash_east = copy.deepcopy(prototype_dash)
dash_east.name = '华东区分视图'
dash_east.filters = ['华东'] # 修改筛选条件

dash_sourth = copy.deepcopy(prototype_dash)
dash_sourth.name = '华南区分视图'
dash_sourth.filters = ['华南']

print(f'克隆耗时：{time.time() - start:.4f} s')

# 3. 验证结果
print('\n--- 3. 验证独立性 ---')
prototype_dash.show()
dash_east.show()
dash_sourth.show()