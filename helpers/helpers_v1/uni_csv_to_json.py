import csv
import json
import random
import re

''''
['CAMPUS_TRADING_NAME',
'coordinates',
'EDUCATION_SECTOR',
'EDUCATIONAL_FACILITY_PROVIDER_CODE',
'EDUCATIONAL_FACILITY_COMPANY_NAME',
'EDUCATIONAL_FACILITY_TRADING_NAME',
'LOCATION_NAME',
'CITY_REGIONAL_FLAG',
'AREA',
'Source',
'UNIVERSITY_CAMPUS_LONG',
'UNIVERSITY_CAMPUS_LAT',
'Cambodia',
'Canada',
'China',
'France',
'Hong Kong',
'India',
'Indonesia',
'Ireland',
'Italy',
'Japan',
'Korea, Republic of (South)',
'Macau',
'Malawi',
'Malaysia',
'Malta',
'Myanmar, The Republic of the Union of',
'Nepal',
'Netherlands',
'Pakistan',
'Papua New Guinea',
'Philippines',
'Portugal',
'Russian Federation',
'Saudi Arabia',
'Singapore',
'South Africa',
'Sri Lanka',
'Sweden',
'Taiwan',
'Thailand',
'Turkey',
'Ukraine',
'United Arab Emirates',
'United Kingdom British - Citizen',
'United Kingdom British - National (Overseas)',
'United States of America',
'Venezuela, Bolivarian Republic of',
'Vietnam',
'Zambia',
'Zimbabwe']
'''

def row_to_obj(data):
    # print data
    # random.randint(1,101),
    coords = data[1][2:-1].split(", ")
    return {
        "name": data[0],
        "shim": re.sub('[^0-9a-zA-Z]+', '-', data[0].lower()),
        "coords": {
            "lat": float(coords[0]),
            "lng": float(coords[1])
        }
    }


with open('int_student_intermediate_data.csv', "r", encoding='latin-1') as csvfile:
    readr = csv.reader(csvfile, delimiter=',')
    initial = next(readr)
    # print initial
    for line in readr:
        print(json.dumps(row_to_obj(line)))
    # print initial
    # for row in readr:
    #   print ', '.join(row)