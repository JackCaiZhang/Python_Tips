# wechatpay_factory.py
from payment_processor import PaymentProcessor
from payment_factory import PaymentFactory
from wechatpay_processor import WechatPayProcessor

class WechatPayFactory(PaymentFactory):
    """
    具体工厂：专门生产微信支付处理器
    """
    def create_processor(self) -> PaymentProcessor:
        # 它知道如何“正确地”初始化一个微信支付产品
        return WechatPayProcessor()