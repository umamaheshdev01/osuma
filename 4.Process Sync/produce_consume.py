import threading
import time

N = 2
flag = [False] * N
turn = 0


def producer():

    while True :

        global turn
        global flag

        while flag[1] and turn==1:
            pass

        print('Producer')
        time.sleep(1)
    
        flag[0] = False
        turn = 1
        flag[1]=True

def consumer():

    while True:

        global turn
        global flag

        while flag[0] and turn==0:
            pass

        print('Consumer')
        time.sleep(1)
        
        flag[1] = False
        turn = 0
        flag[0] =  True
        

producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

producer_thread.start()
consumer_thread.start()

producer_thread.join()
consumer_thread.join()

