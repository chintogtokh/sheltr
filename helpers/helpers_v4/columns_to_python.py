import csv
import json
import random
import re

cols = []
with open('IE_DATA_COMP_2_05_2018.csv', "r", encoding='latin-1') as csvfile:
    readr = csv.reader(csvfile, delimiter=',')
    cols = next(readr)

#print stats for use
idx=0
for i in cols:
    print('"' + re.sub('[^0-9a-zA-Z]+', '-', i.lower()) + '": {"number": data[' + str(idx) +  '], "year": "2016"},')
    idx+=1