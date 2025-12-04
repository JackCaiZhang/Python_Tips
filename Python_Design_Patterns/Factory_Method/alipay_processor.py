# alipay_processor.py
from payment_processor import PaymentProcessor

class AlipayProcessor(PaymentProcessor):
    """
    具体产品：支付宝支付
    """
    def __init__(self):
        print('初始化...加载支付宝 SDK')
        # self.alipay_client = ...

    def pay(self, amount):
        print(f'通过【支付宝】支付了 {amount} 元。')