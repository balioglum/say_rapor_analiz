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

html_file="/root/malsay_html_files/ANKARA BÜYÜKŞEHİR BELEDİYESİ_2019.html"

html_file = open(html_file,'r').read()
soup = BeautifulSoup(html_file, 'html.parser')

soup_text=soup.text
print(type(soup_text))
