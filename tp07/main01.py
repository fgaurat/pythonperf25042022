#!/usr/bin/env python

import threading
import time

the_lock = threading.Lock()

def traitement_long_1():
    with the_lock:
        for i in range(10):
            print(f'traitement_long_1 {i}')
            time.sleep(0.3)



def traitement_long_2():
    with the_lock:    
        for i in range(10):
            print(f'traitement_long_2 {i}')
            time.sleep(0.3)




def main():

    # traitement_long_1()
    # traitement_long_2()

    th1 = threading.Thread(target=traitement_long_1)
    th2 = threading.Thread(target=traitement_long_2)
    th1.start()
    th2.start()

    th1.join()
    th2.join()

if __name__ == '__main__':
    main()