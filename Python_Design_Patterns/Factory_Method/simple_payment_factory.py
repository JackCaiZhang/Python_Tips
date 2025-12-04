# simple_payment_factory.py
from payment_processor import PaymentProcessor
from wechatpay_processor import WechatPayProcessor
from alipay_processor import AlipayProcessor

# “捷径”：使用字典分发（简单工厂模式）
class SimplePaymentFactory:
    def __init__(self):
        # 维护一个“产品注册表”
        self._processors = {
            'wechat': WechatPayProcessor,   # 注意，这里存的是类本身，不是实例
            'alipay': AlipayProcessor
        }

    def register_processor(self, pay_type: str, processor_class: PaymentProcessor) -> None:
        """允许动态注册新的支付方式"""
        self._processors[pay_type] = processor_class

    def create_processor(self, pay_type: str) -> PaymentProcessor:
        """通过查找字典来创建产品"""
        process_class = self._processors.get(pay_type)
        if not process_class:
            raise ValueError(f'不支持的支付类型：{pay_type}')
        
        # 依然利用了多态性，因为它们都继承自 PaymentProcessor
        return process_class()
    
# --- 客户端使用 ---
factory = SimplePaymentFactory()
# 假如 ApplePayProcessor 也在别处定义好了
# factory.register_processor('apple_pay', ApplyPayProcessor) # 轻松扩展

processor_wechat = factory.create_processor('wechat')
processor_wechat.pay(77)

processor_alipay = factory.create_processor('alipay')
processor_alipay.pay(88)