#!/usr/bin/env python

from Carre import Carre
from Cercle import Cercle
from Rectangle import Rectangle


def show_surface(o):
    print("show_surface")
    print(o.surface)

def main():
    r = Rectangle(longueur=2,largeur=5)
    c = Carre(cote=2)
    ce = Cercle(rayon=2)
    print(c.cote)
    print(c.surface)
    c.cote=3
    print(c.surface)
    print(c)
    print(ce)
    print(ce.surface)

    show_surface(r)
    show_surface(c)
    show_surface(ce)

if __name__ == '__main__':
    main()