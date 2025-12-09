from abc import ABC, abstractmethod

# --- 抽象产品 A：存储服务 ---
class Storage(ABC):
    @abstractmethod
    def save(self, data: str):
        pass

# --- 抽象产品 B：消息队列 ---
class Queue(ABC):
    @abstractmethod
    def push(self, message: str):
        pass