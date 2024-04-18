import queue
import threading
import time
import random

class BoundedBuffer:
    def __init__(self, max_size):
        self.buffer = queue.Queue(max_size)
        self.max_size = max_size

    def put(self, item):
        self.buffer.put(item)

    def get(self):
        return self.buffer.get()

def producer(buffer, producer_id):
    while True:
        item = random.randint(1, 100)
        buffer.put(item)
        print(f"Producer {producer_id} produced item: {item}")
        time.sleep(random.random())  

def consumer(buffer, consumer_id):
    while True:
        item = buffer.get()
        print(f"Consumer {consumer_id} consumed item: {item}")
        time.sleep(random.random()) 

if __name__ == "__main__":
    
    buffer_size = 10
    buffer = BoundedBuffer(buffer_size)

    num_producers = 3
    num_consumers = 2

    producer_threads = []
    for i in range(num_producers):
        thread = threading.Thread(target=producer, args=(buffer, i))
        thread.start()
        producer_threads.append(thread)

    consumer_threads = []
    for i in range(num_consumers):
        thread = threading.Thread(target=consumer, args=(buffer, i))
        thread.start()
        consumer_threads.append(thread)

    for thread in producer_threads + consumer_threads:
        thread.join()
