#!/usr/bin/env python

from Rectangle import Rectangle
from DRectangle import DRectangle


def main():
    r = DRectangle(longueur=1,largeur=2)

    print(r.longueur)
    print(r.surface)

def main01():
    r = Rectangle(longueur=12,largeur=5) # constuire un rectangle de longueur 12 et  largeur 5
    r0 = Rectangle()
    r1 = Rectangle(longueur=12,largeur=5) # constuire un rectangle de longueur 12 et  largeur 5
    r2 = Rectangle.build_from_str('1,2')
    # print("Rectangle.get_cpt()",Rectangle.get_cpt("toto"))
    # print("r.get_cpt()",r.get_cpt("toto"))
    # print(r2)
    r.longueur = 100
    r.longueur = 50
    r.longueur = 200
    # longueur = r.longueur
    # print(longueur) # je devrais avoir : 12
    # # assert r.longueur ==12
    # surface = r.surface # 60
    # print(surface)

    # r.longueur = 2
    # print(r.longueur) # 2



    # the_string = str(r)
    # print(the_string)

    # i = int(r)
    # print(i)


    # # if r.__eq__(r1):
    # if r==r1:
    #     print("ok")
    # else:
    #     print("ko")


    # print(r.longueur)
    # print(r.largeur)
    # print(r.surface)
    # r.longueur = 12
    # print(r.surface)
if __name__ == '__main__':
    main()