import threading
import time

# def worker():
#     print("Worker thread starting")
#     time.sleep(2)
#     print("Worker thread finished")
#
# t = threading.Thread(target=worker)
# t.start()   # 创建并启动线程
# t.join()    # 阻塞主线程，直到子线程结束
# print("Main thread finished")

# 线程传参
# def worker(name, delay):
#     print(f"Worker {name} starting")
#     time.sleep(delay)
#     print(f"Worker {name} finished")
#
# t = threading.Thread(target=worker, args=("T1", 2))
# t.start()

# 自定义线程类（OOP写法）
# class MyThread(threading.Thread):
#     def __init__(self, name, delay):
#         super().__init__()
#         self.name = name
#         self.delay = delay
#
#     def run(self):
#         print(f"Thread {self.name} starting")
#         time.sleep(self.delay)
#         print(f"Thread {self.name} finished")
#
# t = MyThread("T2", 3)
# t.start()


# -------------------------- 线程同步 --------------------------
# 1. Lock（最常用）
# 情况：两个线程同时修改同一个全局变量 → 数据错误
# lock = threading.Lock()
# counter = 0
# def add():
#     global counter
#     for _ in range(1000000):
#         with lock:
#             counter += 1
#
# t1 = threading.Thread(target=add)
# t2 = threading.Thread(target=add)
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print("Final counter (without lock):", counter)

# 使用线程池下载网页
# import requests
# from concurrent.futures import ThreadPoolExecutor
#
# def fetch_url(url):
#     try:
#         response = requests.get(url, timeout=5)
#         return url, response.status_code
#     except Exception as e:
#         return url, str(e)
#
# urls = [
#     "https://www.baidu.com",
#     "https://www.python.org",
#     "https://www.github.com",
#     "https://www.stackoverflow.com",
#     "https://www.invalid-url-example.com"
# ]
#
# with ThreadPoolExecutor(max_workers=5) as executor:
#     futures = [executor.submit(fetch_url, url) for url in urls]
#     for future in futures:
#         url, status = future.result()
#         print(f"URL: {url}, Status: {status}")

# 爬取 100 个网页（IO 密集 → 多线程飞快）
import requests
import time
from concurrent.futures import ThreadPoolExecutor

urls = [f'https://httpbin.org/delay/1'] * 100

def fetch(url):
    response = requests.get(url)
    return 'ok'

start_time = time.time()
with ThreadPoolExecutor(max_workers=20) as executor:
    results = list(executor.map(fetch, urls))

print(f'耗时：{time.time() - start_time} 秒')