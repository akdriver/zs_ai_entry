from concurrent.futures.thread import ThreadPoolExecutor


def ak47(fname):
    return "hello"


with ThreadPoolExecutor(max_workers=2) as executors:
    names = ["A","B","C","D","E","F"]
    futures = [executors.submit(ak47,(name,)) for name in names]
    for future in futures:
        print(future.result())

