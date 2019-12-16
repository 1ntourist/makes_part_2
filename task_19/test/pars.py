from bs4 import BeautifulSoup
import requests
from pprint import pprint
import csv

url = 'https://lalafo.kg/kyrgyzstan/mobilnye-telefony-i-aksessuary/mobilnye-telefony'

def get_html(url):
    r = requests.get(url)
    return r.text

def write_csv(data):
    with open('lalafo.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow( {data ['name'], data ['price']})

def get_contents(html):
    soup = BeautifulSoup(html, 'html.parser')
    blocks = soup.find('div', class_ = 'mr-3').find_all('div', class_ = 'listing-item-main')
    for block in blocks:
        name = block.find('a').text
        price = block.find('p', class_ = 'listing-item-title').text.strip()
        data = {'name' : name, 'price' : price }
        write_csv(data)

get_contents(get_html(url))
