import requests
from pprint import pprint
from bs4 import BeautifulSoup
import csv
from datetime import datetime
from multiprocessing import Pool


url = 'https://lalafo.kg/kyrgyzstan/mobilnye-telefony-i-aksessuary/mobilnye-telefony/apple-iphone?currency=KGS'


def get_html(url):
    r = requests.get(url)
    return r.text

def write_csv(data):
    with open('lalafo.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow( {data ['name'], data ['price']})

def get_urls(html):
    soup = BeautifulSoup(html, 'html.parser')
    blocks = soup.find('div', class_ = 'mr-3').find_all('div', class_ = 'listing-item-main')
    for block in blocks:
        try:
            name = block.find('a').text
        except:
            name = ' '
        try:
            price = block.find('p', class_ = 'listing-item-title').text.strip()
        except:
            price = ' '


        data = {'name' : name, 'price' : price }

        write_csv(data)
        # pprint(name)
        # pprint(price)
        # pprint(data)


get_urls(get_html(url))
