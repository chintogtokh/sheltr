import csv
import json
import random
import re

cols = []
with open('ITERATION_2_TMP.csv', "r", encoding='latin-1') as csvfile:
    readr = csv.reader(csvfile, delimiter=',')
    cols = next(readr)

#print stats for use
idx=102
for i in cols[0:10]:
    print('"' + i + '": {"number": data[' + str(idx) +  '], "year": "2016"},')
    idx+=1