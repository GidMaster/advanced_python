"""
Multithreading
"""
import threading
import time

tLock = threading.Lock()

def timer(name, delay, repeat):
    print(f'Timer: {name} Started')
    tLock.acquire()
    print(f'{name} has acquired the lock')
    while repeat > 0:
        time.sleep(delay)
        print(f'{name}: {str(time.ctime(time.time()))}')
        repeat -= 1
    print(f'{name} is releasing the lock')
    tLock.release()
    print(f'Timer: {name} Completed')

def main():
    t1 = threading.Thread(target=timer, args=('Timer1', 1, 5))
    t2 = threading.Thread(target=timer, args=('Timer2', 2, 5))
    t1.start()
    t2.start()

    print('Main is completed')

if __name__ == '__main__':
    main()