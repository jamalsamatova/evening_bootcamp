import requests
from bs4 import BeautifulSoup as BS

TOTAL_PAGES = 6

def get_html(url):
    response = requests.get(url)
    return response.text

def get_data(html):
    soup = BS(html, 'lxml')
    grid = soup.find('div', class_ = 'grid-deputs')
    deputy_items = grid.find_all('div', class_ = 'dep-item')
    deputy_info = []
    for deputy in deputy_items:
        name = deputy.find('a', class_ = 'name').text
        fraction = deputy.find('div', class_ = 'info').text
        deputy_info.append((name, fraction))
    return deputy_info


def main():
    deputy_info = []
    for page in range(1, TOTAL_PAGES):
        url = f'http://kenesh.kg/ru/deputy/list/35?page={page}'
        deputy_info.extend(get_data(get_html(url)))
    print(deputy_info)
    return deputy_info

if __name__ == '__main__':
    main()