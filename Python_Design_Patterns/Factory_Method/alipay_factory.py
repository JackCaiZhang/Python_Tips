# alipay_factory.py
from payment_processor import PaymentProcessor
from payment_factory import PaymentFactory
from alipay_processor import AlipayProcessor

class AlipayFactory(PaymentFactory):
    """
    具体工厂：专门生产支付宝处理器
    """
    def create_processor(self) -> PaymentProcessor:
        return AlipayProcessor()