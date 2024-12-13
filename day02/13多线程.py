import time
import threading

def multi_task(name,delay):
    for i in range(5):
        time.sleep(delay)  # 模拟任务
        print(f"线程 {name}: 执行第 {i+1} 次")

# 创建一个thread对象， 直接使用 threading.Thread
thread1 = threading.Thread(target=multi_task,args=("first",1))
thread2 = threading.Thread(target=multi_task,args=("second",1))

# 启动线程
thread1.start()
thread2.start()
time.sleep(2)
print("main threading started.")

# 在主线程调用thread1.join()方法，等待thread1 线程执行完成，主线程才会结束
thread1.join()
thread2.join()
print("main threading ended.")

class CustomThread(threading.Thread):
    def __init__(self,name,delay):
        super().__init__()
        self.name = name
        self.delay = delay

    def run(self):
        for i in range(5):
            time.sleep(self.delay)
            print(f"Thread:{self.name} is executing for the {i} time")

ct1 = CustomThread("ct1",1)
ct2 = CustomThread("ct2",1)

ct1.start()
ct2.start()


# 使用锁 解决线程安全问题
lock = threading.Lock()
shared_count = 0

def add_count(times):
    global shared_count
    for _ in range(times):
        with lock:
            shared_count+=1

shared_thread1 = threading.Thread(target=add_count,args=(1000000,))
shared_thread2 = threading.Thread(target=add_count,args=(1000000,))

shared_thread1.start()
shared_thread2.start()
shared_thread1.join()
shared_thread2.join()

print(shared_count)


