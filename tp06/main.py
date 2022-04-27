#!/usr/bin/env python

from CustomerDAO import CustomerDAO


def main():
    
    customerDAO = CustomerDAO('data.csv')

    for customer in customerDAO.find_all():
        print(customer.email)

    for customer in customerDAO.find_done():
        print(customer.done)


if __name__ == '__main__':
    main()