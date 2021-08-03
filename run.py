import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template

app=Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/Detik-Populer')

def detik_populer():
    url = 'https://www.detik.com/terpopuler'
    tag = 'tag_from'
    html_doc = requests.get((url), params={(tag): 'wp_cb_mostPopular_more'})
    soup = BeautifulSoup(html_doc.text, 'html.parser')
    # print(html_doc.text)
    populer_area = soup.find(attrs={'class': 'grid-row list-content'})

    titles = populer_area.findAll(attrs={'class': 'media__title'})
    images = populer_area.findAll(attrs={'class': 'media__image'})

    return render_template('index.html', images=images)








if __name__=='__main__':
    app.run(debug=True)