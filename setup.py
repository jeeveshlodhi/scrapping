import requests
from bs4 import BeautifulSoup
import re
import math
from multiprocessing.pool import ThreadPool
import csv

def scrape(link):
    # links = ["https://uk.rs-online.com/web/c/batteries-chargers/battery-charger-accessories/battery-charger-leads/"]

    while True:
        try:
            page = requests.get(link)
            if page.status_code == 200 :
                soup = BeautifulSoup(page.content, 'html.parser')
                pdesc = soup.find_all('td',class_="descriptionCol")
                for r in pdesc:
                    with open('data.csv','a+', encoding='utf8',newline="") as file:
                        write = csv.writer(file)
                        write.writerow(re.findall(r'target="_self">(.*?)</a>',str(r)))
                    file.close()
        except:
            continue
        break

def run_downloader(process:int, page_url:list):
    """
    Inputs:
        process: (int) number of process to run
        images_url:(list) list of images url
    """
    print(f'MESSAGE: Running {process} process')
    results = ThreadPool(process).imap_unordered(scrape, page_url)          
    count = 0
    for r in results:
        #print(r)
        print(count)
        count+=1

num_process = 8
f1=open("link.csv","r")
links =f1.readlines()
l = []
for link in links:
    l.append(link)
run_downloader(num_process, l)

