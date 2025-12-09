from abstract_factory import InfrastructureFactory
from abstract_factory import Storage, Queue
from concrete_product import S3Storage, SQSQueue, FileSystemStorage, MemoryQueue

# === AWS 工厂 ===
class AWSFactory(InfrastructureFactory):
    def create_storage(self) -> Storage:
        return S3Storage()  # 锁死：AWS 工厂只生产 S3
    
    def create_queue(self) -> Queue:
        return SQSQueue()   # 锁死：AWS 工厂只生产 SQS
    
# === 本地工程 ===
class LocalFactory(InfrastructureFactory):
    def create_storage(self):
        return FileSystemStorage()
    
    def create_queue(self):
        return MemoryQueue()