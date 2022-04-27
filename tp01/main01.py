import monmodule as lemodule
from monmodule import add as the_add
import sys
import copy



def add(a, b):
    print(a, b)


def main_01():
    print("Hello")
    print(__name__)  # __main__. dunder main => double underscore main
    a = lemodule.add(1, 2)
    print(a)
    a = add(1, 2)
    print(a)


def main_02():
    a = "Hello"  # immutable
    print(hex(id(a)))
    a = 'Toto' # inférence de type
    b = 'Toto'
    c =True
    d =1.2
    # a[0] = "B"
    print(a)  # ?Bello

    print(hex(id(a)))
    print(hex(id(b)))

    print("getrefcount",sys.getrefcount(1))
    val1 = 1
    print("getrefcount",sys.getrefcount(1))
    val2 = 1
    print("getrefcount",sys.getrefcount(1))

    print("val1",hex(id(val1)))
    print("val2",hex(id(val2)))

    print(type(a))
    print(type(val1))
    print(type(c))
    print(type(d))



def main():
    l = [10,20,30,40,50]
    l[1] = 1000
    print(type(l))
    l1 = l[2:4] # 2,inc : 4:exclu
    print(l1) # [30,40]
    l1 = l[2:]
    print(l1) # [30,40,50]
    l1 = l[:3]
    print(l1) # [10,20,30]
    l1 = l[:] # shallow copy
    l2 = l # assignement, affectation
    print(hex(id(l)))
    print(hex(id(l2)))

    print(hex(id(l1)))
    l2[1] = 65
    print(l)
    print(l1)

    m = [
        [0,1],
        [2,3],
        [4,5],
    ]

    m1 = m[:]
    m2 = copy.deepcopy(m)

    print(hex(id(m)))
    print(hex(id(m1)))
    m1[1][0] = 15
    m2[1][0] = 150
    
    print(m)


if __name__ == '__main__':
    main()
