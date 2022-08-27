import pandas as pd
from dataclasses import dataclass
from bs4 import BeautifulSoup
import regex as re
import os
from pathlib import Path
import glob

lower_map = {
    ord(u'A'): u'a',
    ord(u'B'): u'b',
    ord(u'C'): u'c',
    ord(u'Ç'): u'ç',
    ord(u'D'): u'd',
    ord(u'E'): u'e',
    ord(u'F'): u'f',
    ord(u'G'): u'g',
    ord(u'Ğ'): u'ğ',
    ord(u'H'): u'h',
    ord(u'I'): u'ı',
    ord(u'İ'): u'i',
    ord(u'J'): u'j',
    ord(u'K'): u'k',
    ord(u'L'): u'l',
    ord(u'M'): u'm',
    ord(u'N'): u'n',
    ord(u'O'): u'o',
    ord(u'Ö'): u'ö',
    ord(u'P'): u'p',
    ord(u'R'): u'r',
    ord(u'S'): u's',
    ord(u'Ş'): u'ş',
    ord(u'T'): u't',
    ord(u'U'): u'u',
    ord(u'Ü'): u'ü',
    ord(u'V'): u'v',
    ord(u'Y'): u'y',
    ord(u'Z'): u'z'
    }
pd.set_option('display.max_rows', None)

#hesap kodları listesi
df= pd.read_csv("/root/hesap_kodlar/hesap_plan.csv", delimiter=";")
df["ARANACAK"]=df["HESAP_KOD"].astype(str)+" "+df["HESAP_ADI"]
#df=pd.read_csv('/root/hesap_kodlar/hesap_plan_tum.csv', delimiter=";",encoding='utf-8-sig')
# df["ARANACAK"]=df["HESAP_ADI"]
print(df)

directory = '/root/malsay_html_files'
temp = []
count=[]
kurum=[]
hesap_kod=df.ARANACAK.str.strip().tolist()
for filename in  sorted(glob.glob(f'{directory}/*')): 
    html_read = open(filename,'r').read()
    soup = BeautifulSoup(html_read, 'html.parser')
    soup_text=soup.text
    string=soup_text.translate(lower_map)
    #print(string)

    for element in hesap_kod:
            temp.append(element) #hesap kodu, aranacak 
            count.append(string.count(element.translate(lower_map))) # html'den oluşturulan stringin içinde element kaç defa geçiyor!
            kurum.append(Path(filename).stem) #kurum adı, html dosya adından alıyor
            
a=list(zip(kurum,temp,count))


df = pd.DataFrame(a, columns =['KURUM','HESAP', 'FREKANS'])
df=df[df['FREKANS'] > 0]

print(df)
df.to_csv('/root/hesap_kodlar/sonuç.csv', index=False)

