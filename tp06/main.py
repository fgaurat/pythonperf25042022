#!/usr/bin/env python

import contextlib
from CustomerDAO import CustomerDAO
import time

class TimePerf(contextlib.ContextDecorator):
    def __enter__(self):
        self.start_time = time.perf_counter()
        print('Starting')
        return self

    def __exit__(self, *exc):
        self.end_time = time.perf_counter()
        print(f'Finishing in {self.end_time-self.start_time} s.')
        return False


@contextlib.contextmanager
def a_function(filename):
    file = open(filename)
    print("enter")
    try:
        yield file
    finally:
        print("exit")
        file.close()


@TimePerf()
def slow_function():
    print("slow_function")
    time.sleep(2)
    # a=2/0


def main():
    slow_function()




def main03():
    with a_function('data.csv') as f:
        for line in f:
            print(line.strip())

    print(f.closed)

    



def main02():
    
    customerDAO = CustomerDAO('data.csv')

    print("start context")
    with customerDAO as dao:
        for customer in customerDAO.find_all():
            print(customer.email)
            a = 2/0
    print("after context")





def main01():
    
    customerDAO = CustomerDAO('data.csv')

    for customer in customerDAO.find_all():
        print(customer.email)

    for customer in customerDAO.find_done():
        print(customer.done)


if __name__ == '__main__':
    main()