from abc import ABC, abstractmethod
from typing import List

class MetricComponent(ABC):
    """Component: 无论是原子指标还是复合指标，都是 MetricComponent"""
    
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculate(self) -> float:
        """核心业务逻辑：计算数值"""
        pass

    def add(self, component):
        """
        默认不支持添加子节点。
        只有 Composite 才会重写这个方法。
        这样设计是为了安全（透明性 vs 安全性的权衡）。
        """
        raise NotImplementedError(f"{self.name} 是叶子节点，不能添加子节点")
    
class AtomicMetric(MetricComponent):
    """Leaf: 最底层的原子指标，无法再分"""
    
    def __init__(self, name, value):
        super().__init__(name)
        self._value = value

    def calculate(self) -> float:
        # 真实场景可能是查数据库或调 API
        print(f"  [Leaf] 计算 {self.name}: {self._value}")
        return self._value
    
class CompositeMetric(MetricComponent):
    """Composite: 容器节点，可以包含任意 Component（Leaf 或 Composite）"""
    
    def __init__(self, name):
        super().__init__(name)
        self._children: List[MetricComponent] = []

    def add(self, component: MetricComponent):
        self._children.append(component)
        return self  # 支持链式调用

    def remove(self, component: MetricComponent):
        self._children.remove(component)

    def calculate(self) -> float:
        print(f"[Group] 开始汇总 {self.name}...")
        total = 0
        for child in self._children:
            # 关键点：这里直接调用 child.calculate()
            # 根本不关心 child 是原子指标还是另一个复合指标
            total += child.calculate()
        
        print(f"[Group] {self.name} 汇总完成: {total}")
        return total
    
# --- 构建一棵复杂的树 ---

# 1. 创建叶子 (原子指标)
m_shanghai = AtomicMetric("上海GMV", 100)
m_hangzhou = AtomicMetric("杭州GMV", 80)
m_beijing = AtomicMetric("北京GMV", 120)

# 2. 创建树枝 (区域指标)
east_region = CompositeMetric("华东区")
east_region.add(m_shanghai).add(m_hangzhou) # 包含两个叶子

north_region = CompositeMetric("华北区")
north_region.add(m_beijing) # 包含一个叶子

# 3. 创建树根 (全国总指标)
china_total = CompositeMetric("全国总GMV")
# 注意：这里 add 的是 Composite 对象！
china_total.add(east_region).add(north_region) 

# --- 客户端调用 ---

def run_report(metric: MetricComponent):
    """
    Client: 我根本不知道传进来的是一个简单的数字，还是整个公司的报表
    我只管调 calculate()
    """
    result = metric.calculate()
    print(f"\n>>> 最终报告结果: {result}")

# 运行
run_report(china_total)