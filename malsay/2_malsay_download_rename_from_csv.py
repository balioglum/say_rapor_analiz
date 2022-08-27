
# PDF'leri download ediyor
import urllib.request
import csv
import os

with open('kurum_links.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    
    for row in reader:
        new_filename = f"/root/malsay_files/{row['KURUM']}_{row['YIL']}.pdf"
        if not os.path.isfile(new_filename): #check if file exists
            urllib.request.urlretrieve(row['LINK'], new_filename)