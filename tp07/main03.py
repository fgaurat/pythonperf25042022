#!/usr/bin/env python


from multiprocessing import Pool
import multiprocessing

def f(x):
    return x*x


def main():
    print(multiprocessing.cpu_count())
    with Pool(2) as p:
        # print(p.map(f, range(10000000)))
        a = p.map(f, range(100000000))

if __name__ == '__main__':
    main()  