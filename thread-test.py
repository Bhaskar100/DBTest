import  threading
import time


def thread1():
    for i in range(10):
        print('thread 1- running')
        time.sleep(3)

def thread2():
    for i in range(10):
        print('thread 2- running')
        time.sleep(3)

t1 = threading.Thread(target=thread1)
t2 = threading.Thread(target=thread2)
tt = threading.currentThread().isDaemon()
print(tt)
t1.start()
t1.join()
t2.start()