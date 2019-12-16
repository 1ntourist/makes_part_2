import requests
from bs4 import BeautifulSoup
import csv

def get_html(url):
    r = requests.get(url)
    return r.text

def get_total_pages(html):
    soup = BeautifulSoup(html, 'html.parser')
    pages = soup.find('div', class_ = 'pagination-pages').find_all('a', class_ = 'pagination-page')[-1].get('href')
    total_pages = pages.split('=')[1].split('&')[0]

    return int(total_pages)

def write_csv(data):
    with open('avito.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow( (data['title'], data['url'], data['price']) )

def get_page_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    ads = soup.find('div', class_ = 'catalog-list js-catalog-list clearfix')#.find_all('div', class_ = 'item_item_table')
    for ad in ads:
        try:
            title = ad.find('div', class_ = 'item_table-description').find('h3').text.strip()
        except:
            title = ''
        try:
            url =title = 'https://www.avito.ru' + ad.find('div', class_ = 'item_table-description').find('h3').find('a').get('href')
        except:
            url = ''
        try:
            price = ad.find('div', class_ = 'about').text.strip()
        except:
            price = ''


        data = {'title': title,
                'url': url,
                'price':price}
        write_csv(data)


def main():
    url = 'https://www.avito.ru/rossiya/telefony?p=1&q=htc'
    base_url = 'https://www.avito.ru/rossiya/telefony?'
    page_part = 'p='
    query_part = '&q=htc'

    total_pages = get_total_pages(get_html(url))

    for i in range(1, total_pages):
        url_gen = base_url + page_part + str(i) +query_part
        html = get_html(url_gen)
        get_page_data(html)

if __name__ == '__main__':
    main()
