from abstract_factory import InfrastructureFactory
from concrete_factory import AWSFactory, LocalFactory

class DataProcessor:
    def __init__(self, factory: InfrastructureFactory):
        # 依赖注入工厂，而不是具体的类
        self.storage = factory.create_storage()
        self.queue = factory.create_queue()

    def process(self, data):
        print('>>> 开始处理业务逻辑...')
        # 1. 存数据
        self.storage.save(data)
        # 2. 发通知
        self.queue.push('Data Processed')
        print('>>> 业务结束。\n')

if __name__ == '__main__':
    # --- 场景模拟 ---
    # 1. 生产环境（Prod）
    print('--- 环境：Production (AWS) ---')
    prod_factory = AWSFactory()
    app_prod = DataProcessor(factory=prod_factory)
    app_prod.process('User_Order_123')

    # 2. 开发环境（Dev）
    print('--- 环境：Local (Dev) ---')
    dev_factory = LocalFactory()
    app_dev = DataProcessor(factory=dev_factory) # 代码逻辑完全没变，只需换个工厂
    app_dev.process('Test_Data_001')