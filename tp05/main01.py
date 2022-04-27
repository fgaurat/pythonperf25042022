#!/usr/bin/env python

class TheList:

    def __init__(self):
        self._data = [f'data {i}' for i in range(10)]

    @property
    def data(self):
        return self._data
        # # from file
        # for data in [f'data {i}' for i in range(10)]:
        #     yield data


def main():
    t = TheList()

    for i in t.data:
        print(i)

if __name__ == '__main__':
    main()