# payment_factory.py
from abc import ABC, abstractmethod
from payment_processor import PaymentProcessor

class PaymentFactory(ABC):
    """
    所有工厂的“规矩”：必须有一个 create_processor 方法。
    这个方法就是“工厂方法”。
    """
    @abstractmethod
    def create_processor(self) -> PaymentProcessor:
        """
        这就是“工厂方法”，它返回一个“产品”
        """
        pass
