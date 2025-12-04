# wechatpay_processor.py
from payment_processor import PaymentProcessor

class WechatPayProcessor(PaymentProcessor):
    """
    具体产品：微信支付
    它可能由自己独特的初始化逻辑
    """
    def __init__(self):
        print('初始化...连接微信支付网关')
        # self.wechat_sdk = ...

    def pay(self, amount):
        print(f'通过【微信】支付了 {amount} 元。')