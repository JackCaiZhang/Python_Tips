from payment_factory import PaymentFactory
from wechatpay_factory import WechatPayFactory
from alipay_factory import AlipayFactory

def process_order(factory: PaymentFactory, amount: float):
    """
    处理订单的函数：它只依赖“工厂的抽象”
    """
    print(f'开始处理订单，金额 {amount}...')

    # 客户端不再关心“如何创建”
    # 它也不关心“是哪种支付方式”
    processor = factory.create_processor()

    # 它只关心“产品能干活”（调用 pay 方法）
    processor.pay(amount)
    print('订单处理完毕。')

# --- 见证“开闭原则”的威力 ---
if __name__ == '__main__':
    # 场景1：客户选择使用微信支付
    print('--- 场景1：微信支付 ---')
    wechat_factory =WechatPayFactory()
    process_order(wechat_factory, 100.0)

    # 场景2：客户选择支付宝支付
    print('\n--- 场景2：支付宝支付 ---')
    alipay_factory = AlipayFactory()
    process_order(alipay_factory, 50.0)