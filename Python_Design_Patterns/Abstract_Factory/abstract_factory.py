from abc import ABC, abstractmethod
from abstract_product import Storage, Queue

# --- 抽象工厂 ---
class InfrastructureFactory(ABC):
    """
    基建工厂接口：它保证生产出来的 Storage 和 Queue 是一套
    """
    @abstractmethod
    def create_storage(self) -> Storage:
        pass

    @abstractmethod
    def create_queue(self) -> Queue:
        pass