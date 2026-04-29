from threading import Thread
import time


def countdown(n):
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(2)


# Create and launch a thread
t = Thread(target=countdown, args=(10, ))
t.start()

if t.is_alive():
    print('Still running')
else:
    print('Completed')
