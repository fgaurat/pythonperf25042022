#!/usr/bin/env python

import asyncio
from pprint import pprint
import time
import random

final_result = []

async def producer(q):
    for i in range(100):
        q.put_nowait(i)

async def consumer(q_in,q_out,name):
    while True:
        item = await q_in.get()
        print(name,item)
        result = (item,item**2,name)
        q_in.task_done()
        q_out.put_nowait(result)
        await asyncio.sleep(random.randint(1,2) )

async def writer(q_out):
    while True:
        result = await q_out.get()
        final_result.append(result)
        print("writer",result)
        q_out.task_done()



async def main():
    q_in = asyncio.Queue()
    q_out = asyncio.Queue()
    task_consumers = [asyncio.create_task(consumer(q_in,q_out,f"consumer {i}"))  for i in range(10)]
    task_producer = asyncio.create_task(producer(q_in))
    task_writer = asyncio.create_task(writer(q_out))
    
    await asyncio.gather(task_producer)
    await q_in.join()

    for t in task_consumers:
        t.cancel()
    
    pprint(final_result)

if __name__ == '__main__':
    asyncio.run(main())