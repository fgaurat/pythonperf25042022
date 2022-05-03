#!/usr/bin/env python
import asyncio
import time


async def add(a,b):
    await asyncio.sleep(1)
    return a+b

async def main():
    s = time.perf_counter()
    r = await asyncio.gather(add(1,2),add(2,2),add(3,2))
    print(r)
    print(f"{time.perf_counter() - s}")



async def main01():
    s = time.perf_counter()
    print('Hello ...')
    # await asyncio.sleep(1)
    c = await add(1,2)
    print(c)
    c = await add(1,2)
    print(c)
    c = await add(1,2)
    print(c)
    print('... World!')
    print(f"{time.perf_counter() - s}")


if __name__ == '__main__':
    # start Event Loop
    asyncio.run(main())
