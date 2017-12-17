"""
Async write
"""

import threading
import time

class AsyncWrite(threading.Thread):

    def __init__(self, text, out):
        threading.Thread.__init__(self)
        self.text = text
        self.out = out

    def run(self):
        f = open(self.out, 'a')
        f.write(self.text + '\n')
        f.close()
        time.sleep(2)
        print(f'Finished Background file write to {self.out}')

def main():
    message = input('Enter the string to store:')
    background = AsyncWrite(message, 'out.txt')
    background.start()
    print('The program can continue while it writes in another thread')
    print('100 + 400 = ', 100 + 400)

    background.join()
    print('wainted until thread was complete.')

if __name__ == '__main__':
    main()