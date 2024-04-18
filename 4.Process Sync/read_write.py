import threading
import time

count = 1
lock = 0

def reader():
        
        while True :
                global lock
                global count

                while lock == 1 : pass
                lock = 1
                print(f'Reader is reading value {count}')
                lock = 0
                time.sleep(1)



def writer():
        
        while True:
                global lock
                global count

                while lock == 1 : pass
                lock = 1
                count+=1
                print(f'Writer Updates the value to {count}')
                lock = 0
                time.sleep(1)


reader1 = threading.Thread(target=reader)
writer1 = threading.Thread(target=writer)

writer1.start()
reader1.start()

reader1.join()
writer1.join()

