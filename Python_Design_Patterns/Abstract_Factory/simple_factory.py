from abstract_product import Storage, Queue
from concrete_product import S3Storage, SQSQueue, FileSystemStorage, MemoryQueue

# 极简版抽象工厂（Python 特供）
class SimpleFactory:
    def __init__(self, storage_cls: Storage, queue_cls: Queue):
        self.storage_cls = storage_cls
        self.queue_cls = queue_cls

    def create_storage(self):
        return self.storage_cls()
    
    def create_queue(self):
        return self.queue_cls()

# 配置
aws_config = SimpleFactory(S3Storage, SQSQueue)
local_config = SimpleFactory(FileSystemStorage, MemoryQueue)