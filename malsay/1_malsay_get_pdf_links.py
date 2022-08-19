#from selenium.webdriver.chrome.options import Options

import re
import time
from pprint import pprint
import pandas as pd
from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.common.by import By

opts = FirefoxOptions()
opts.add_argument("--headless")
browser = webdriver.Firefox(options=opts)



""" chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--profile-directory=Default')
chrome_options.add_argument('--user-data-dir=~/.config/google-chrome')

browser = webdriver.Chrome(options=chrome_options) """


top_html="https://www.sayistay.gov.tr/reports/category/31-belediyeler---bagli-idareler"
browser.get(top_html)
html = browser.page_source
#print(html)
links=[]
kurum=[]
yil=[]
cols = ['KURUM', 'YIL', 'LINK']
elems = browser.find_elements(by=By.XPATH, value='//a[@href]') 

for elem in elems:
    
    if re.match(r"https:\/\/www\.sayistay\.gov\.tr\/reports\/[0-9]{4}.*", str(elem.get_attribute("href"))):
        e=elem.get_attribute("href").strip()
        first_part = e[0:36]
        last_part=e[36:]
        rapor_link=f"{first_part}download/{last_part}"
        print(f"{first_part}download/{last_part}")
        links.append(rapor_link)
        
        kurumun_ismi=elem.get_attribute("text").strip()
        kurum_ad, rapor_yil = kurumun_ismi[:-4].strip(), kurumun_ismi[-4:].strip()
        kurum.append(kurum_ad)
        yil.append(rapor_yil)
        
        print(f"{kurum_ad}_{rapor_yil}")
        
data_tuples = list(zip(kurum,yil,links))
#time.sleep(5)
df = pd.DataFrame(data_tuples, columns=cols)

print(df)
# with open(r'/root/malsay/raporlinks.csv', 'w') as fp:
#     fp.write('\n'.join(links))

df.to_csv('kurum_links.csv',index=False, header=True)



