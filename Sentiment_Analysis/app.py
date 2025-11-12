# app.py
from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from datetime import datetime
import logging

from models import (
    SentimentRequest,
    SentimentResponse,
    BatchSentimentRequest,
    BatchSentimentResponse,
    HealthResponse,
    ErrorResponse
)
from sentiment_predict import predict_with_confidence
from config import settings

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# 创建FastAPI应用
app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="一个功能完善的情感分析API服务，支持单条和批量文本分析",
    docs_url="/docs",
    redoc_url="/redoc"
)

# 添加CORS中间件
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 生产环境应该限制具体域名
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 全局异常处理器
@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    logger.error(f"Unhandled exception: {str(exc)}", exc_info=True)
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content=ErrorResponse(
            error="Internal Server Error",
            detail="An unexpected error occurred"
        ).model_dump()
    )

@app.get("/", response_model=dict, tags=["Root"])
async def root():
    """根路径，返回基本信息"""
    return {
        "message": f"Welcome to {settings.app_name}",
        "version": settings.app_version,
        "docs": "/docs",
        "health": "/health"
    }

@app.get("/health", response_model=HealthResponse, tags=["Health"])
async def health_check():
    """健康检查端点"""
    return HealthResponse(
        status="healthy",
        app_name=settings.app_name,
        version=settings.app_version
    )

@app.post(
    "/predict",
    response_model=SentimentResponse,
    status_code=status.HTTP_200_OK,
    tags=["Sentiment Analysis"],
    summary="分析单条文本情感",
    description="对单条文本进行情感分析，返回情感类别和置信度"
)
async def analyze_sentiment(request: SentimentRequest):
    """
    分析单条文本的情感倾向
    
    - **text**: 待分析的文本内容
    
    返回：
    - **sentiment**: 情感类别 (positive/negative/neutral)
    - **confidence**: 置信度 (0-1)
    - **timestamp**: 分析时间
    """
    try:
        logger.info(f"Analyzing single text: {request.text[:50]}...")
        sentiment, confidence = predict_with_confidence(request.text)
        
        response = SentimentResponse(
            text=request.text,
            sentiment=sentiment,
            confidence=round(confidence, 4)
        )
        
        logger.info(f"Analysis result: {sentiment} (confidence: {confidence:.4f})")
        return response
        
    except Exception as e:
        logger.error(f"Error analyzing sentiment: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to analyze sentiment: {str(e)}"
        )

@app.post(
    "/predict/batch",
    response_model=BatchSentimentResponse,
    status_code=status.HTTP_200_OK,
    tags=["Sentiment Analysis"],
    summary="批量分析文本情感",
    description="对多条文本进行批量情感分析"
)
async def batch_analyze_sentiment(request: BatchSentimentRequest):
    """
    批量分析多条文本的情感倾向
    
    - **texts**: 待分析的文本列表（最多100条）
    
    返回：
    - **results**: 每条文本的分析结果
    - **total_count**: 总数量
    """
    try:
        logger.info(f"Analyzing batch of {len(request.texts)} texts")
        
        results = []
        for text in request.texts:
            sentiment, confidence = predict_with_confidence(text)
            results.append(
                SentimentResponse(
                    text=text,
                    sentiment=sentiment,
                    confidence=round(confidence, 4)
                )
            )
        
        response = BatchSentimentResponse(
            results=results,
            total_count=len(results)
        )
        
        logger.info(f"Batch analysis completed: {len(results)} texts processed")
        return response
        
    except Exception as e:
        logger.error(f"Error in batch analysis: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to analyze batch: {str(e)}"
        )

@app.get(
    "/statistics",
    tags=["Statistics"],
    summary="获取统计信息",
    description="返回服务的基本统计信息"
)
async def get_statistics():
    """获取服务统计信息"""
    return {
        "model_name": settings.model_name,
        "supported_sentiments": ["positive", "negative", "neutral"],
        "max_batch_size": 100,
        "max_text_length": 5000
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app:app",
        host=settings.host,
        port=settings.port,
        reload=settings.debug
    )
