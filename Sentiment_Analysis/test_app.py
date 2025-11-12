# test_app.py
import pytest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

class TestRootEndpoints:
    """测试根端点"""
    
    def test_root(self):
        """测试根路径"""
        response = client.get("/")
        assert response.status_code == 200
        data = response.json()
        assert "message" in data
        assert "version" in data
        assert "docs" in data
    
    def test_health_check(self):
        """测试健康检查"""
        response = client.get("/health")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "healthy"
        assert "app_name" in data
        assert "version" in data

class TestSentimentAnalysis:
    """测试情感分析功能"""
    
    def test_positive_sentiment(self):
        """测试积极情感"""
        response = client.post(
            "/predict",
            json={"text": "I love this product! It's amazing and wonderful!"}
        )
        assert response.status_code == 200
        data = response.json()
        assert data["sentiment"] == "positive"
        assert "confidence" in data
        assert 0 <= data["confidence"] <= 1
    
    def test_negative_sentiment(self):
        """测试消极情感"""
        response = client.post(
            "/predict",
            json={"text": "This is terrible and awful. I hate it!"}
        )
        assert response.status_code == 200
        data = response.json()
        assert data["sentiment"] == "negative"
        assert "confidence" in data
    
    def test_neutral_sentiment(self):
        """测试中性情感"""
        response = client.post(
            "/predict",
            json={"text": "This is a car."}
        )
        assert response.status_code == 200
        data = response.json()
        assert data["sentiment"] == "neutral"
        assert "confidence" in data
    
    def test_negation_handling(self):
        """测试否定词处理"""
        response = client.post(
            "/predict",
            json={"text": "This is not good at all."}
        )
        assert response.status_code == 200
        data = response.json()
        # "not good" 应该被识别为负面
        assert data["sentiment"] in ["negative", "neutral"]
    
    def test_empty_text(self):
        """测试空文本"""
        response = client.post(
            "/predict",
            json={"text": ""}
        )
        # 应该返回验证错误
        assert response.status_code == 422
    
    def test_long_text(self):
        """测试长文本"""
        long_text = "good " * 100
        response = client.post(
            "/predict",
            json={"text": long_text}
        )
        assert response.status_code == 200
        data = response.json()
        assert data["sentiment"] == "positive"

class TestBatchAnalysis:
    """测试批量分析功能"""
    
    def test_batch_analysis(self):
        """测试批量分析"""
        response = client.post(
            "/predict/batch",
            json={
                "texts": [
                    "I love this!",
                    "This is terrible.",
                    "It's okay."
                ]
            }
        )
        assert response.status_code == 200
        data = response.json()
        assert "results" in data
        assert "total_count" in data
        assert data["total_count"] == 3
        assert len(data["results"]) == 3
        
        # 检查每个结果
        assert data["results"][0]["sentiment"] == "positive"
        assert data["results"][1]["sentiment"] == "negative"
        assert data["results"][2]["sentiment"] in ["neutral", "positive"]
    
    def test_empty_batch(self):
        """测试空批量"""
        response = client.post(
            "/predict/batch",
            json={"texts": []}
        )
        # 应该返回验证错误
        assert response.status_code == 422
    
    def test_single_item_batch(self):
        """测试单条文本的批量分析"""
        response = client.post(
            "/predict/batch",
            json={"texts": ["This is great!"]}
        )
        assert response.status_code == 200
        data = response.json()
        assert data["total_count"] == 1
        assert len(data["results"]) == 1

class TestStatistics:
    """测试统计端点"""
    
    def test_get_statistics(self):
        """测试获取统计信息"""
        response = client.get("/statistics")
        assert response.status_code == 200
        data = response.json()
        assert "model_name" in data
        assert "supported_sentiments" in data
        assert "max_batch_size" in data
        assert "max_text_length" in data
        assert set(data["supported_sentiments"]) == {"positive", "negative", "neutral"}

class TestResponseStructure:
    """测试响应结构"""
    
    def test_sentiment_response_structure(self):
        """测试情感分析响应结构"""
        response = client.post(
            "/predict",
            json={"text": "This is good"}
        )
        assert response.status_code == 200
        data = response.json()
        
        # 检查所有必需字段
        assert "text" in data
        assert "sentiment" in data
        assert "confidence" in data
        assert "timestamp" in data
        
        # 检查数据类型
        assert isinstance(data["text"], str)
        assert isinstance(data["sentiment"], str)
        assert isinstance(data["confidence"], (int, float))
        assert isinstance(data["timestamp"], str)

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
