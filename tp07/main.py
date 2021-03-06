#!/usr/bin/env python
from bs4 import BeautifulSoup
import requests
import time
import multiprocessing
# import multiprocessing.pool.Threadpool


def download_file(url):
    resp = requests.get(url)
    with open(url.split('/')[-1],"w") as f:
        print(resp.text,file=f,end="")



def main():
    url = "http://logs.eolem.com/"
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    links = [f"{url}{a['href']}" for a in soup.find_all('a') if a['href'][0] != '?']
    
    start_time = time.perf_counter()

    with multiprocessing.Pool() as p:
        p.map(download_file, links)
    
    # 0.364055523 sans multiprocessing
    # 0.688740203 avec multiprocessing
    print(time.perf_counter() - start_time)

if __name__ == '__main__':
    main()