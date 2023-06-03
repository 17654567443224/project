author:'2021402010226 李效闻'
import functools
import time

def retry(max_retries=5, sleep_time=1):
    """出错重试装饰器"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            retries = 0
            while retries < max_retries:
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception as e:
                    retries += 1
                    print(f"连接失败重连: {e}. 重试 {sleep_time} 次")
                    time.sleep(sleep_time)
            print(f"最大重试次数 ({max_retries}) 已达到，gg")
        return wrapper
    return decorator