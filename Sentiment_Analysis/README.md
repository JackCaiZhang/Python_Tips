# 情感分析 API 项目

一个基于 FastAPI 框架开发的完整情感分析 API 服务，支持单条和批量文本情感分析。

## 项目特性

- ✨ **完整的 REST API** - 提供标准的 RESTful 接口
- 🚀 **高性能** - 基于 FastAPI 和 Uvicorn，异步处理
- 📊 **多种功能** - 单条分析、批量分析、统计信息
- 🔍 **智能分析** - 支持否定词处理和置信度评估
- 📝 **自动文档** - 自动生成交互式 API 文档
- ✅ **完整测试** - 包含全面的单元测试
- 🛡️ **错误处理** - 完善的异常处理机制
- 📦 **易于部署** - 支持多种部署方式

## 项目结构

```
.
├── app.py                  # FastAPI 主应用
├── models.py              # Pydantic 数据模型
├── sentiment_predict.py   # 情感分析核心逻辑
├── config.py              # 配置文件
├── test_app.py            # 测试文件
├── requirements.txt       # 项目依赖
└── README.md              # 项目文档
```

## 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 运行服务

```bash
# 方式一：直接运行
python app.py

# 方式二：使用 uvicorn
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

### 3. 访问文档

服务启动后，访问以下地址：

- **交互式文档 (Swagger UI)**: http://localhost:8000/docs
- **ReDoc 文档**: http://localhost:8000/redoc
- **API 根路径**: http://localhost:8000/

## API 端点

### 1. 根路径
```
GET /
```
返回 API 基本信息

### 2. 健康检查
```
GET /health
```
检查服务健康状态

### 3. 单条文本分析
```
POST /predict
```

**请求体:**
```json
{
  "text": "I love this product!"
}
```

**响应:**
```json
{
  "text": "I love this product!",
  "sentiment": "positive",
  "confidence": 0.85,
  "timestamp": "2025-11-11T10:00:00"
}
```

### 4. 批量文本分析
```
POST /predict/batch
```

**请求体:**
```json
{
  "texts": [
    "I love this!",
    "This is terrible.",
    "It's okay."
  ]
}
```

**响应:**
```json
{
  "results": [
    {
      "text": "I love this!",
      "sentiment": "positive",
      "confidence": 0.9,
      "timestamp": "2025-11-11T10:00:00"
    },
    ...
  ],
  "total_count": 3
}
```

### 5. 统计信息
```
GET /statistics
```

返回模型和服务的统计信息

## 使用示例

### Python 示例

```python
import requests

# 单条分析
response = requests.post(
    "http://localhost:8000/predict",
    json={"text": "This is amazing!"}
)
print(response.json())

# 批量分析
response = requests.post(
    "http://localhost:8000/predict/batch",
    json={
        "texts": [
            "I love it!",
            "Terrible experience.",
            "It's okay."
        ]
    }
)
print(response.json())
```

### cURL 示例

```bash
# 单条分析
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{"text": "This is wonderful!"}'

# 批量分析
curl -X POST "http://localhost:8000/predict/batch" \
  -H "Content-Type: application/json" \
  -d '{"texts": ["Great!", "Bad!", "Okay."]}'
```

## 运行测试

```bash
# 运行所有测试
pytest test_app.py -v

# 运行特定测试类
pytest test_app.py::TestSentimentAnalysis -v

# 查看测试覆盖率
pytest test_app.py --cov=. --cov-report=html
```

## 配置说明

在 `config.py` 中可以配置以下参数：

```python
app_name: str = "Sentiment Analysis API"
app_version: str = "1.0.0"
debug: bool = False
host: str = "0.0.0.0"
port: int = 8000
model_name: str = "simple_rule_based"
confidence_threshold: float = 0.6
```

也可以通过创建 `.env` 文件来覆盖默认配置：

```bash
DEBUG=true
PORT=8080
```

## 情感分析算法

当前使用基于规则的情感分析方法：

1. **词汇匹配** - 使用预定义的积极/消极词汇表
2. **否定词处理** - 识别 "not good" 等否定结构
3. **置信度计算** - 基于情感词数量和分布
4. **三分类** - positive、negative、neutral

### 特性

- 支持否定词翻转（如 "not good" → negative）
- 基于情感词数量计算置信度
- 文本预处理和标准化

## 扩展建议

可以通过以下方式增强项目：

1. **机器学习模型** - 集成 BERT、RoBERTa 等预训练模型
2. **数据库** - 添加分析历史记录存储
3. **缓存** - 使用 Redis 缓存常见查询
4. **认证** - 添加 API Key 或 OAuth2 认证
5. **限流** - 实现请求速率限制
6. **多语言** - 支持中文等其他语言
7. **情感强度** - 返回情感强度分数
8. **实体识别** - 提取关键实体及其情感

## 依赖说明

主要依赖包：

- **FastAPI** - Web 框架
- **Uvicorn** - ASGI 服务器
- **Pydantic** - 数据验证
- **Pytest** - 测试框架

详见 `requirements.txt`

## 部署

### Docker 部署

可以创建 `Dockerfile` 进行容器化部署：

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY .. .
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
```

### 生产部署建议

1. 使用 Gunicorn + Uvicorn workers
2. 配置 Nginx 反向代理
3. 启用 HTTPS
4. 设置适当的 CORS 策略
5. 添加日志收集和监控

## 许可证

MIT License

## 贡献

欢迎提交 Issue 和 Pull Request！

## 联系方式

如有问题，请通过 Issue 反馈。
