# import PyPDF2

# path="/root/malsay/deneme_pdf/ADANA BÜYÜKŞEHİR BELEDİYESİ_2020.pdf"
# text=""
# pdf_file = open(path, 'rb')
# text =""
# read_pdf = PyPDF2.PdfFileReader(pdf_file)
# c = read_pdf.numPages
# for i in range(c):  
#     print(i)
#     page = read_pdf.getPage(i)
#     text+=(page.extractText())

# print(text)

from pdf2docx import Converter

pdf_file = "/root/malsay/deneme_pdf/ADANA BÜYÜKŞEHİR BELEDİYESİ_2017.pdf"
docx_file = "/root/malsay/deneme_pdf/ADANA BÜYÜKŞEHİR BELEDİYESİ_2017.docx"

# convert pdf to docx
cv = Converter(pdf_file)
cv.convert(docx_file, multi_processing=True, cpu_count=2)     # all pages by default
cv.close()

#convert docx to html
import mammoth
import os

filename_html=f"{os.path.splitext(docx_file)[0]}.html"
print (filename_html)
with open(f"/root/malsay_docx_files/{docx_file}", "rb") as docx_file:
    result = mammoth.convert_to_html(docx_file)
    html = result.value # The generated HTML
    messages = result.messages # Any messages, such as warnings during conversion

    #print(html)
    print(messages)
    
file = open(filename_html,"w")

file.write(html)
file.close()
    