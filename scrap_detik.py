import requests
from bs4 import BeautifulSoup

html_doc = requests.get('https://www.detik.com/terpopuler', params={'tag_from': 'wp_cb_mostPopular_more'})

soup = BeautifulSoup(html_doc.text, 'html.parser')

populer_area = soup.find(attrs={'class':'grid-row list-content'})

titles = populer_area.findAll(attrs={'class':'media__title'})
images = populer_area.findAll(attrs={'class':'media__image'})

#for judul in titles:
#    print(judul.text)

for gambar in images:
    print(gambar.find('a').find('img')['title'])

#print(titles)