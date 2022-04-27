#!/usr/bin/env python
import sys
def division(a,b):
    return a/b

def call_division(a,b):
    r = 0
    try:
        r = division(a,b)
    # except Exception as e:
    #     print(e)
    #     raise e
    # else:
    #     print("ça vaaaaa")
    finally:
        print("la suite de call_division")
    return r


def main():
    a = 2
    b = int(input("Valeur de b: "))
    c = call_division(a,b)
    print("resultat",c)

def main01():
    try:
        a = 2

        # toto = True if a==2 else False


        b = int(input("Valeur de b: "))
        c = call_division(a,b)
    except (ZeroDivisionError, TypeError) as e:
        print("error !", e)
    except Exception as e:
        print("Exception error !", e)

        sys.exit()

    else:
        print("pas d'erreur !")
    
    print("la suite")


if __name__ == '__main__':
    main()
