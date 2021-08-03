import requests
from bs4 import BeautifulSoup

url = 'https://www.detik.com/terpopuler'
tag = 'tag_from'
html_doc=requests.get((url), params={(tag): 'wp_cb_mostPopular_more'})
soup=BeautifulSoup(html_doc.text, 'html.parser')
#print(html_doc.text)
populer_area=soup.find(attrs={'class':'grid-row list-content'})

titles=populer_area.findAll(attrs={'class':'media__title'})
images=populer_area.findAll(attrs={'class':'media__image'})

#for title in titles:
#    print (title.text)

for image in images:
    print (image.find('a').find('img')['title'])

