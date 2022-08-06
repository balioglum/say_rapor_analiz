from bs4 import BeautifulSoup
import re

filename_html="/root/malsay/deneme_pdf/ADANA BÜYÜKŞEHİR BELEDİYESİ_2017.html"
html_file = open(filename_html,'r').read()
soup = BeautifulSoup(html_file, 'html.parser')

for content in soup.find_all(['strong'], text = re.compile("^Bulgu\s\d.*", re.IGNORECASE)):
#for content in soup.find_all(['p']):

    x=content.text
    x=str(x)
    print(x)

    