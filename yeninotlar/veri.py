"""
import requests
from bs4 import BeautifulSoup

r = requests.get('https://freebitco.in/')
soup = BeautifulSoup(r.content, 'html.parser')
list = soup.find_all('a')
for link in list:
    print(link.text,link.get('href'))
"""
"""
import requests
from bs4 import BeautifulSoup
import operator

def sozlukolustur(tumkelimeler):
    kelimesayisi = {}
    for kelime in tumkelimeler:
        if kelime in kelimesayisi:
            kelimesayisi[kelime] += 1
        else:
            kelimesayisi[kelime] = 1
    return kelimesayisi

url = "https://shiftdelete.net/hash-nedir-sha-256-algoritmasi/"

tumkelimeler = []

r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')

for kelimegruplari in soup.find_all('p'):
    icerik = kelimegruplari.text
    kelimeler = icerik.lower().split()
    for kelime in kelimeler:
        tumkelimeler.append(kelime)

kelimesayisi = sozlukolustur(tumkelimeler)

for anahtar, deger in sorted(kelimesayisi.items(),key = operator.itemgetter(0)):
    print(anahtar, deger)
"""
# belirli class i alamadik