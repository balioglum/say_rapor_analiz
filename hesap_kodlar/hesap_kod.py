import pandas as pd
from dataclasses import dataclass
from bs4 import BeautifulSoup
import regex as re
import os
from pathlib import Path

pd.set_option('display.max_rows', None)

#hsap kodları listesi
df= pd.read_csv("/root/hesap_kodlar/hesap_plan.csv", delimiter=";")
df["ARANACAK"]=df["HESAP_KOD"].astype(str)+" "+df["HESAP_ADI"]


html_file="/root/malsay_html_files/ANKARA BÜYÜKŞEHİR BELEDİYESİ_2019.html"
html_file = open(html_file,'r').read()
soup = BeautifulSoup(html_file, 'html.parser')

soup_text=soup.text
#soup_text="895 BÜTÇE Hesabı"
#print(soup_text)
#print(df.ARANACAK.tolist())
def counting(string, hesap_kod):
    temp = []
    count=[]
    for element in hesap_kod:
        temp.append(element)
        count.append(string.count(element))
       # temp.append('{} count is {}'.format(element, string.count(element)))
    return list(zip(temp,count)) #', '.join(temp)

a=counting(soup_text.upper(),df.ARANACAK.tolist())
df = pd.DataFrame(a, columns =['HESAP', 'FREKANS'])

print(df)

# if any(ext in df.ARANACAK.tolist() for ext in soup_text):
#     print(ext)

