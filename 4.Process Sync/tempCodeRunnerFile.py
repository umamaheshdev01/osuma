import threading
import time

class BinarySemaphore:
    def __init__(self):
        self.value = True  

    def acquire(self):
        while not self.value:
            pass
        self.value = False 

    def release(self):
        self.value = True 


counter = 0
lock = BinarySemaphore()


def increment_counter():
    global counter
    lock.acquire()
    try:
        counter += 1
        print(f"Counter value increased to {counter}")
        time.sleep(1)
    finally:
        lock.release()


def decrement_counter():
    global counter
    lock.acquire()
    try:
        counter -=1
        print(f"Counter value decreased to {counter}")
        time.sleep(1)
    finally:
        lock.release()



threads = []
threads.append(threading.Thread(target=increment_counter))
threads.append(threading.Thread(target=decrement_counter))


for thread in threads:
    thread.start()


for thread in threads:
    thread.join()

print('Done')