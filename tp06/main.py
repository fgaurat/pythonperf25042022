#!/usr/bin/env python

import contextlib
from CustomerDAO import CustomerDAO

@contextlib.contextmanager
def a_function(filename):
    file = open(filename)
    print("enter")
    try:
        yield file
    finally:
        print("exit")
        file.close()


def main():
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