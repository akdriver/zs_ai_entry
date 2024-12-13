import threading
import queue
import time
from queue import Queue


def producer(q:queue.Queue):
    while True:
        time.sleep(1)
        print("producer generated one")
        q.put("123")


def consumer(q:queue.Queue):
    while True:
        time.sleep(1)
        item = q.get()  # 从队列中取出数据
        print(f"消费者：消费 {item}")

q = queue.Queue(maxsize=5)
# 创建线程
producer_thread = threading.Thread(target=producer, args=(q,))
consumer_thread = threading.Thread(target=consumer, args=(q,))

producer_thread.start()
consumer_thread.start()

producer_thread.join()
consumer_thread.join()