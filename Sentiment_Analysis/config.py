# config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Sentiment Analysis API"
    app_version: str = "1.0.0"
    debug: bool = False
    host: str = "0.0.0.0"
    port: int = 8000
    
    # 模型相关配置
    model_name: str = "simple_rule_based"
    confidence_threshold: float = 0.6
    
    class Config:
        env_file = ".env"
        case_sensitive = False

settings = Settings()
