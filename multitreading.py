"""
Multithreading
"""
from threading import Thread
import time

def timer(name, delay, repeat):
    print(f'Timer: {name} Started')
    while repeat > 0:
        time.sleep(delay)
        print(f'{name}: {str(time.ctime(time.time()))}')
        repeat -= 1
    print(f'Timer: {name} Completed')

def main():
    t1 = Thread(target=timer, args=('Timer1', 1, 5))
    t2 = Thread(target=timer, args=('Timer2', 2, 5))
    t1.start()
    t2.start()

    print('Main is completed')

if __name__ == '__main__':
    main()