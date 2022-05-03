#!/usr/bin/env python
from tasks import add


def main():

    a = add.delay(4, 4)
    print(a.get())

if __name__ == '__main__':
    main()