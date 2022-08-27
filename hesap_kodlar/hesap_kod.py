#BUNU KULLANMIYORUM, 
# hesap_plan.csv dosyasındaki ARANACAK listesini, HTML dosyasının içinde arıyor!
# TEK BİR HTML DOSYASINDA ARIYOR KELİMELERİ, bir klasdördeki tüm html dosyalarına bakmak için->> hesap_kod_LOOP.py
import pandas as pd
from dataclasses import dataclass
from bs4 import BeautifulSoup
import regex as re
import os
from pathlib import Path

pd.set_option('display.max_rows', None)

#hsap kodları listesi
df= pd.read_csv("/home/ubuntu/say_rapor_analiz/hesap_kodlar/hesap_plan.csv", delimiter=";")
df["ARANACAK"]=df["HESAP_KOD"].astype(str)+" "+df["HESAP_ADI"]


html_file="/home/ubuntu/say_rapor_analiz/malsay_html_files/ANKARA BÜYÜKŞEHİR BELEDİYESİ_2019.html"
html_file_to_read = open(html_file,'r').read()
soup = BeautifulSoup(html_file_to_read, 'html.parser')

soup_text=soup.text
#soup_text="895 BÜTÇE Hesabı"
#print(soup_text)
#print(df.ARANACAK.tolist())
temp = []
count=[]
kurum=[]
def counting(string, hesap_kod):
    
    for element in hesap_kod:
        temp.append(element)
        count.append(string.count(element))
        kurum.append(Path(html_file).stem)
       # temp.append('{} count is {}'.format(element, string.count(element)))
    return list(zip(kurum,temp,count)) #', '.join(temp)

a=counting(soup_text.upper(),df.ARANACAK.tolist())
df = pd.DataFrame(a, columns =['KURUM','HESAP', 'FREKANS'])

print(df)

# if any(ext in df.ARANACAK.tolist() for ext in soup_text):
#     print(ext)

