from abstract_product import Storage, Queue

# === 套装 1：AWS 风格 ===
class S3Storage(Storage):
    def save(self, data):
        print(f'【AWS S3】正在上传数据：{data}')

class SQSQueue(Queue):
    def push(self, message):
        print(f'【AWS S3】发消息到云端：{message}')

# === 套装 2：本地开发风格 ===
class FileSystemStorage(Storage):
    def save(self, data):
        print(f'【Local File】写入本地硬盘：{data}')

class MemoryQueue(Queue):
    def push(self, message):
        print(f'【Local Memory】压入内存列表：{message}')