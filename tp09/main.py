
import time
import timeit

#!/usr/bin/env python

def the_loop():
    l = [10,20,30,40]
    r = []
    for i in l:
        r.append(i*2)

def the_map():
    l = [10,20,30,40]
    result = list(map(lambda a:a*2,l))

def the_comp():
    l = [10,20,30,40]
    r = [i*2 for i in l]




def main():

    t1 = timeit.timeit('the_loop()',setup="from __main__ import the_loop")
    t2 = timeit.timeit('the_map()',setup="from __main__ import the_map")
    t3 = timeit.timeit('the_comp()',setup="from __main__ import the_comp")

    print(f"{t1=}")
    print(f"{t2=}")
    print(f"{t3=}")

    
def main01():
    s = time.perf_counter()
    the_loop()
    print(f"{time.perf_counter() - s}")

    s = time.perf_counter()
    the_map()
    print(f"{time.perf_counter() - s}")

    s = time.perf_counter()
    the_comp()
    print(f"{time.perf_counter() - s}")


if __name__ == '__main__':
    main()