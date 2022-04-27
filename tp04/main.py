#!/usr/bin/env python

from Rectangle import Rectangle
from ICalcGeo import ICalcGeo

# __call__ : créer la classe
# __new__ : (cls) créer l'instance à partir de la classe
# __init__ : (self) initialiser l'instance

def main():
    i = ICalcGeo()
    r = Rectangle(longueur=1,largeur=2)
    r1 = Rectangle(longueur=10,largeur=20)
    # r = Rectangle.get_instance()
    # r1 = Rectangle.get_instance()

    print(hex(id(r)))
    print(hex(id(r1)))

    print(r)
    print(r1)

    r1.longueur = 12
    print(r)
    print(r1)


    print(type(type))

if __name__ == '__main__':
    main()