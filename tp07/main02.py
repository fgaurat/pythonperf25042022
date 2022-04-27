#!/usr/bin/env python


import threading
import time

the_lock = threading.Lock()


class MonThread(threading.Thread):
    
    def __init__(self) -> None:
        super().__init__()


    def run(self):
        with the_lock:
            for i in range(10):
                print(f'{self.name} {i}')
                time.sleep(0.3)


def main():
    th1 = MonThread()
    th2 = MonThread()
    
    th1.start()
    th2.start()


if __name__ == '__main__':
    main()