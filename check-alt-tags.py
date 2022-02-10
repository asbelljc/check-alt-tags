import sys
import requests
from bs4 import BeautifulSoup
from pprint import pprint

website = input('Enter URL ')

if website[ : 7] != 'http://' and website[ : 8] != 'https://':
    website = 'http://' + website

r = requests.get(website)
source = r.content
soup = BeautifulSoup(r.content)

images = soup.find_all('img', alt='')
urls = []

for img in images:
    urls.append(img['src'])

for index, url in enumerate(urls):
    print(str(index + 1) + ': ' + url)
    if index != len(urls) - 1:
        print('----------------------------------------')

print()
