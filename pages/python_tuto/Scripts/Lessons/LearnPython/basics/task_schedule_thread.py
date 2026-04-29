import pause
import webbrowser
from datetime import datetime
from threading import Thread


def open_browser():
    pause.until(datetime(2023, 1, 8, 3, 5, 0))
    webbrowser.open("https://www.baidu.com")


# Create and launch a thread
t = Thread(target=open_browser)
t.start()

if t.is_alive():
    print('Still running')

print('Completed')
