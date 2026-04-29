import threading


class MyThread(threading.Thread):
    def run(self):
        for _ in range(10):
            print(threading.current_thread().getName())


x = MyThread(name='Sending message')
y = MyThread(name='receiving message')

x.start()
y.start()
