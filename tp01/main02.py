#!/usr/bin/env python
import collections
# PEP8
# class = UpperCamelCase
# method = snake_case
# variable ou objet = camelCase
# CONSTANTE => UpperCase 
#snake case

# avant lambda
# def mult_by_2(i):
#     return i*2

def main01():
    l = [10,20,30,40]
    
    # scolaire
    r = []
    for i in l:
        r.append(i*2)
    
    # dev
    # result = list(map(mult_by_2,l))
    result = list(map(lambda a:a*2,l))


    # Pythonic way
    r = [i*2 for i in l]


    l = ["   terter    ","rez  "," ffdgdfg"]
    l1 = [s.strip() for s in l]


    
    print(result)
    # result = [20,40,60,80]


# nombre variable de paramètre positionnel
def add(*args):
    print(type(args))
    a=0
    for i in args:
        a+=i
    return a





# nombre variable de paramètre par keywords
def hello2(**kwargs):
    print(kwargs) # {firstname:"fred",name:"gaurat",toto:12}

# Positional only
def hello(name,firstname,/):
    print(name,firstname)

# Keyword only
def hello(*,name,firstname):
    print(name,firstname)



def main02():

    # list => [...]
    # dict => {x:y,...}
    # set => {...}
    # tuple => (x,y,...)

    # l = [1,2,3,4,5]
    a= 1,2,3,4,5,'toto',1.45,False
    l= [1,2,3,4,5,'toto',1.45,False]
    l.append(456456)

    if not a[-1]:
        print(a[-1])

    p = 1,2,3,4,5
    # r = add(1,2,3,4,5)
    r = add(*p) # 15
    print(r)

    a,b,*c=1,2,5,8,9

    print(a)
    print(b)

    d = {'firstname':'fred','name':"Gaurat",'age':45,'job':'dev'}
    # **d = 'firstname'='fred','name'="Gaurat",'age'=45,'job'='dev'
    # hello("gaurat","fred")
    # print(firstname='fred',name="Gaurat",age=45,job='dev')
    # hello(firstname="fred",name="gaurat",toto=12)
    # hello(**d)
    print(f"{d['firstname']}")
    # print("{firstname} {name}".format(firstname='fred',name="Gaurat",age=45,job='dev'))
    print("{firstname} {name}".format(**d))
    hello("gaurat","fred")
    hello(firstname="fred",name="gaurat")


def main():
    l = [1,2,3]
    q = collections.deque(l)
    print(q)
    q.append(4)
    print(q)
    # q.insert(0,0)
    q.appendleft(10)
    print(q)
    f = q.popleft()
    print(q)

if __name__ == '__main__':
    main()