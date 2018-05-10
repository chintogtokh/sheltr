import csv
import json
import random
import re

def row_to_obj(data):
    # print data
    # random.randint(1,101),
    lat = data[1]
    lng = data[2]
    return {
        "name": data[4],
        "shim": re.sub('[^0-9a-zA-Z]+', '-', data[3].lower()).replace("-distance",""),
        "coords": {
            "lat": float(lat),
            "lng": float(lng)
        }
    }

uni_for_mongo = []
with open('uni_campus_ordered.csv', "r", encoding='latin-1') as csvfile:
    readr = csv.reader(csvfile, delimiter=',')
    initial = next(readr)
    # print initial
    for line in readr:
        uni_for_mongo.append(row_to_obj(line))

with open('uni_for_mongo.txt', "w") as file_to_write:
    for i in uni_for_mongo:
        file_to_write.write(json.dumps(i))
        file_to_write.write("\n")

#print unis for use
idx=102
for i in uni_for_mongo:
    print('"' + i['shim'] +  '": { "number": float(data[' + str(idx) + ']), "year": "2016"},')


print("\n\n\n\n")

#print unis for use
idx=102
for i in uni_for_mongo:
    print('"' + i['shim'] +  '": int(data[' + str(idx) + ']),')
    idx+=1