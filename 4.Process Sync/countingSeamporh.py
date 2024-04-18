import threading
import time

class CountingSemaphore:
    def __init__(self, initial_value):
        self.value = initial_value

    def acquire(self):
        while self.value <= 0:
            pass
        self.value -= 1

    def release(self):
        self.value += 1


resource_pool_size = 3
resource_pool = CountingSemaphore(resource_pool_size)


def task():
    resource_pool.acquire()
    try:
        print("Task acquired a resource.")
        time.sleep(1)
    finally:
        resource_pool.release()
        print("Task released a resource.\n")
        
   


num_tasks = 5
threads = []
for _ in range(num_tasks):
    thread = threading.Thread(target=task)
    threads.append(thread)


for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print("All tasks finished.")
