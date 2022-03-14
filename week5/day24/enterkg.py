# import requests
# from bs4 import BeautifulSoup as bs
# import csv

# def get_html(url):
#     response = requests.get(url)
#     # print(response.status_code)
#     return response.text

# def get_data(html):
#     soup = bs(html, 'lxml')
#     catalog = soup.find('div', class_ = 'browse-view')
#     notebooks = catalog.find_all('div', class_ = 'row')
#     # print(notebooks[0].find('div', class_ = 'rows').find('a').text.strip())
#     # print('https://enter.kg' + notebooks[0].find('a', class_ = 'product-image-link').find('img').get('src'))
#     # print(notebooks[0].find('span', class_ = 'price').text.strip())
#     for note in notebooks:
#         try:
#             title = note.find('div', class_ = 'rows').find('a').text.strip()
#         except:
#             title = ''
#         try:
#             image = 'https://enter.kg' + note.find('a', class_ = 'product-image-link').find('img').get('src')
#         except:
#             image = 'No photo!'
#         try:
#             price = note.find('span', class_ = 'price').text.strip()
#         except:
#             price = ''

#         data = {
#             'title': title, 
#             'image': image, 
#             'price': price,
#         }
#         write_csv(data)

# def write_csv(data):
#     with open('enter_notebooks.csv', 'a') as csv_file:
#         writer = csv.writer(csv_file, delimiter = '/')
#         writer.writerow(
#             (
#                 data['title'],
#                 data['image'],
#                 data['price']
#             )
#         )

# def main():
#     page = 0
#     while page < 11:
#         print(f'Парсинг {page + 1} страницы...')
#         if page == 0:
#             url = 'https://enter.kg/computers/noutbuki_bishkek'
#         else:
#             url = f'https://enter.kg/computers/noutbuki_bishkek/results,{page}01-{page}00'
#         html = get_html(url)
#         get_data(html)
#         page += 1

# main()



# from turtle import title
import requests
from bs4 import BeautifulSoup as bs
import csv

def get_html(url):
  response = requests.get(url)
  return response.text

def get_data(html):
  soup = bs(html, 'lxml')
  for item in soup:
    title = soup.find('div', class_ = 'itemBody').strip().text
    write_csv(title)

def write_csv(data):
  with open('data.csv', 'a') as f:
    writer = csv.writer(f, delimiter = '/')
    writer.writerow(
      data
    )

def main():
  page = 0
  for i in range(1, 21):
    print(f'Парсинг {i} страницы...')
    url = 'https://vesti.kg/itemlist.html?start={page}'
    page += 30
    html = get_html(url)
    get_data(html)

main()