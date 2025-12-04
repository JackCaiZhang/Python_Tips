# payment_processor.py
from abc import ABC, abstractmethod

# 1. 定义“产品”接口（PaymentProcessor）
class PaymentProcessor(ABC):
    """
    所有支付处理器的“规矩”：必须有一个 pay 方法
    """
    @abstractmethod
    def pay(self, amount):
        """支付行为"""
        pass