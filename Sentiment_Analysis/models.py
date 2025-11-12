# models.py
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class SentimentRequest(BaseModel):
    """情感分析请求模型"""
    text: str = Field(..., min_length=1, max_length=5000, description="待分析的文本")
    
    class Config:
        json_schema_extra = {
            "example": {
                "text": "I am very happy today!"
            }
        }

class SentimentResponse(BaseModel):
    """情感分析响应模型"""
    text: str = Field(..., description="原始文本")
    sentiment: str = Field(..., description="情感类别: positive, negative, neutral")
    confidence: float = Field(..., ge=0, le=1, description="置信度")
    timestamp: datetime = Field(default_factory=datetime.now, description="分析时间")
    
    class Config:
        json_schema_extra = {
            "example": {
                "text": "I am very happy today!",
                "sentiment": "positive",
                "confidence": 0.85,
                "timestamp": "2025-11-11T10:00:00"
            }
        }

class BatchSentimentRequest(BaseModel):
    """批量情感分析请求模型"""
    texts: List[str] = Field(..., min_length=1, max_length=100, description="待分析的文本列表")
    
    class Config:
        json_schema_extra = {
            "example": {
                "texts": [
                    "I love this product!",
                    "This is terrible.",
                    "It's okay."
                ]
            }
        }

class BatchSentimentResponse(BaseModel):
    """批量情感分析响应模型"""
    results: List[SentimentResponse]
    total_count: int
    
class HealthResponse(BaseModel):
    """健康检查响应模型"""
    status: str
    app_name: str
    version: str
    timestamp: datetime = Field(default_factory=datetime.now)

class ErrorResponse(BaseModel):
    """错误响应模型"""
    error: str
    detail: Optional[str] = None
    timestamp: datetime = Field(default_factory=datetime.now)
