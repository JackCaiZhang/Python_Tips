import perfplot
import random

# 生成测试数据
def generate(n):
    return [random.randint(0, 1000) for _ in range(n)]

# 去重方法
def using_set(data):
    return list(set(data))

def using_dict(data):
    return list({x: None for x in data}.keys())

def using_loop(data):
    seen = set()
    out = []
    for x in data:
        if x not in seen:
            seen.add(x)
            out.append(x)
    return out

perfplot.show(
    setup=generate,
    kernels=[
        using_set,
        using_dict,
        using_loop,
    ],
    labels=['set()', 'dict()', 'loop()'],
    n_range=[2**k for k in range(8, 20)], # 输入规模
    xlabel='Input size (n)',
    time_unit='ms',
    equality_check=False, # ✨忽略结果是否相同
)