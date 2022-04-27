#!/usr/bin/env python
from do_log import do_log


# HOC higher order function
# Closure
# def make_incrementor(n):
#     return lambda x: x + n

def make_incrementor(n):
    name = "toto"
    def the_function(x):
        print(name)
        return x+n
    
    return the_function




@do_log
def say_hello(name):   
    print("hello",name)

def main():
    # inc_function = make_incrementor(2)

    # print(inc_function(3))
    # print(inc_function(10))

    # wrapper = do_log(say_hello)
    # wrapper("fred")
    
    say_hello('fred')

if __name__ == '__main__':
    main()