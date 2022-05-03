#!/usr/bin/env python
import threading
from bs4 import BeautifulSoup
import requests
import time



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
    for url in links:
        # download_file(url)
        threading.Thread(target=download_file,args=[url]).start()
    
    # 0.364055523 sans thread
    # 0.01630881099999998 avec thread
    print(time.perf_counter() - start_time)
    # th.join()

    # ...


if __name__ == '__main__':
    main()