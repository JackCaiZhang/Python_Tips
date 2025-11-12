# sentiment_predict.py
from typing import Tuple
import re

class SentimentAnalyzer:
    """基于规则的情感分析器"""
    
    def __init__(self):
        # 积极情感词汇
        self.positive_words = {
            'happy', 'good', 'great', 'excellent', 'wonderful', 'fantastic',
            'amazing', 'love', 'like', 'enjoy', 'perfect', 'best', 'beautiful',
            'awesome', 'brilliant', 'superb', 'outstanding', 'delightful',
            'pleased', 'satisfied', 'excited', 'joyful', 'cheerful'
        }
        
        # 消极情感词汇
        self.negative_words = {
            'sad', 'bad', 'terrible', 'horrible', 'awful', 'hate', 'dislike',
            'poor', 'worst', 'disappointing', 'disappointed', 'angry', 'upset',
            'frustrated', 'annoying', 'annoyed', 'depressed', 'unhappy',
            'miserable', 'pathetic', 'disgusting', 'useless', 'failure'
        }
        
        # 否定词
        self.negation_words = {'not', 'no', 'never', 'neither', 'nor', 'nothing', 'nowhere'}
    
    def preprocess_text(self, text: str) -> list:
        """预处理文本，分词并转小写"""
        # 移除标点符号，保留字母和空格
        text = re.sub(r'[^a-zA-Z\s]', '', text.lower())
        # 分词
        words = text.split()
        return words
    
    def calculate_sentiment_score(self, words: list) -> Tuple[float, int, int]:
        """计算情感分数"""
        positive_count = 0
        negative_count = 0
        
        # 检查否定词
        for i, word in enumerate(words):
            # 检查当前词是否被否定
            is_negated = False
            if i > 0 and words[i-1] in self.negation_words:
                is_negated = True
            
            if word in self.positive_words:
                if is_negated:
                    negative_count += 1
                else:
                    positive_count += 1
            elif word in self.negative_words:
                if is_negated:
                    positive_count += 1
                else:
                    negative_count += 1
        
        # 计算情感分数 (-1 到 1)
        total = positive_count + negative_count
        if total == 0:
            score = 0.0
        else:
            score = (positive_count - negative_count) / total
        
        return score, positive_count, negative_count
    
    def predict(self, text: str) -> Tuple[str, float]:
        """预测文本情感
        
        Returns:
            Tuple[str, float]: (sentiment, confidence)
            sentiment: 'positive', 'negative', 'neutral'
            confidence: 0.0 到 1.0
        """
        if not text or not text.strip():
            return 'neutral', 0.5
        
        words = self.preprocess_text(text)
        score, pos_count, neg_count = self.calculate_sentiment_score(words)
        
        # 根据分数确定情感类别
        if score > 0.1:
            sentiment = 'positive'
        elif score < -0.1:
            sentiment = 'negative'
        else:
            sentiment = 'neutral'
        
        # 计算置信度
        total_sentiment_words = pos_count + neg_count
        if total_sentiment_words == 0:
            confidence = 0.5  # 中性情感，置信度为0.5
        else:
            # 置信度基于情感词的数量和分数的绝对值
            confidence = min(0.5 + abs(score) * 0.5, 1.0)
        
        return sentiment, confidence

# 全局分析器实例
_analyzer = SentimentAnalyzer()

def predict(text: str) -> str:
    """预测文本情感（简化接口，保持向后兼容）"""
    sentiment, _ = _analyzer.predict(text)
    return sentiment

def predict_with_confidence(text: str) -> Tuple[str, float]:
    """预测文本情感并返回置信度"""
    return _analyzer.predict(text)
