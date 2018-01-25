from bs4 import BeautifulSoup
from HTMLParser import HTMLParser

bhtml = open("ee.txt", 'r')

soup = BeautifulSoup(bhtml, "html.parser")

# form =  soup.findAll('form')

profilBilgi = soup.find('form', {"name": "mainf"}).findAll('img')

dizi = []

for qq in profilBilgi:
    ee = str(qq)
    ee = ee.split(' ')
    ee = ee[2].split('/')
    ee = ee[2].split('.')
    rr = ee[0]
    dizi.append(rr)
print dizi
