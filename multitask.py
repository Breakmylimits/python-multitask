import time
import threading

def Ae86():
    for i in range(10):
        print('--start--')
        time.sleep(3)

def skyline():
    for i in range(10):
        print('---fast---')
        time.sleep(2)

task1 = threading.Thread(target=Ae86)
task2 = threading.Thread(target=skyline)

task1.start()
task2.start()

task1.join()
task2.join()
