from dataclasses import dataclass
import pandas as pd
from rapidfuzz import fuzz
import glob
from bs4 import BeautifulSoup
import regex as re
from pdf2docx import Converter
import mammoth
import os
from pathlib import Path
 
# assign directory
directory = '/root/malsay_files/' #pdf'lerim olduğu directory
kurum=[]
baslik=[]
yil=[]
cols = ['KURUM', 'YIL', 'BASLIK']
# iterate over files in that directory
# sorted=alfabetik sıra. böylece bir file'da sorun çıkarsa hangisi olduğunu bulmak kolay oluyor.
for filename in  sorted(glob.glob(f'{directory}/*')): 
    bare_filename=Path(filename).stem  # uzantısız pathsiz sadece filename
    print(filename)
    file_in_docxfolder = f"/root/malsay_docx_files/{bare_filename}.docx"
    if not os.path.isfile(file_in_docxfolder): #check if docx file exists in docx folder
      
      #bare_filename_with_path=f"{os.path.splitext(filename)[0]}" #pathli
     
      kurum_ad, rapor_yil = bare_filename[:-4].strip(), bare_filename[-4:].strip()
      #print(filename)
      pdf_file = filename
      docx_file = f"/root/malsay_docx_files/{bare_filename}.docx" #
      
      print(docx_file)
      # convert pdf to docx
      cv = Converter(pdf_file)
      cv.convert(docx_file, multi_processing=True, cpu_count=3) # all pages by default
      cv.close() #kendi klasörüne docx file oluşturup save ettik

      filename_with_html=f"/root/malsay_html_files/{bare_filename}.html" #
      print(filename_with_html)
      with open(docx_file, "rb") as docx_file:
          result = mammoth.convert_to_html(docx_file)
          html = result.value # The generated HTML
          messages = result.messages # Any messages, such as warnings during conversion

          #print(html)
          print(messages)
          
      file = open(filename_with_html,"w")

      file.write(html)
      file.close()
      #BURAYA KADAR HTML DOSYASINI KENDİ KLASÖRÜNE SAVE ETTİK.
      #BURADAN SONRA
      html_file = open(filename_with_html,'r').read()
      soup = BeautifulSoup(html_file, 'html.parser')
      bulgu_list=soup.find_all(['strong'], text = re.compile("^Bulgu\s\d.*", re.IGNORECASE))
      print(bulgu_list)
      #daha sonra yap bunu!
      # for bulgux in bulgu_list:
      #     txt=re.sub(str(bulgux), r'[^<strong>BULGU\s*\d{1,2}:*\s].*[^\s</strong>]', str(bulgux), re.IGNORECASE)
      #     print(txt)
      for bulgu in bulgu_list:
        # print(bulgu)
          print(list(bulgu))
        #  print(list(bulgu_list))
          baslik.append(bulgu.text.strip())
          kurum.append(bare_filename)
          x=bare_filename.split('_')[-1]
          yil.append(x)
        
print(kurum,baslik,yil)

data_tuples = list(zip(kurum,yil,baslik))
print(data_tuples)

df = pd.DataFrame(data_tuples, columns=cols)

print(df)

df.to_csv('kurum_bulgu.csv',index=False, header=True)
    