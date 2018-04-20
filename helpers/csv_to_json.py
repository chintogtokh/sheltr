import csv
import json
import random
import re

def row_to_obj(data):
	# print data
	return {
	    "name": data[2].title(),
	    "population": 12345,
	    "shim": re.sub('[^0-9a-zA-Z]+', '-', data[2].lower()),
	    "rating_safety": random.randint(1,101),
	    "rating_affordability": random.randint(1,101),
	    "outlinks": {
	    "realestate": "http://www.google.com",
	    "domain": "http://www.google.com"
	    },
	    "coords": {
	        "lat": float(data[5]),
	        "lng": float(data[4])
	    }
	}


'''
0
1 LOCATION
2 SUBURB_TOWN_NAME
3 SUBURB_RESIDENTS
4 SUBURB_LONG
5 SUBURB_LAT
6 FID
7 DOMAIN_URL
8 REAL_ESTATE_COM_AU_URL
9 SUBURB_MOST_COMMON_EXPENSE_TIER
10 SUBURB_PRICE_RANGE_RANK
11 SUBURB_PRICE_RANK_IN_PERCENTILE
12 SUBURB_RENTAL_PRICE_SCALE_RANK
13 SUBURB_OFFENCES_PER_10000_POPULATION
14 TOTAL_2016_ADJUSTED_OFFENCES_PER_SUBURB_TOWN_NAME
15 SUBURB_TOWN_NAME_2016_ADJUSTED_CRIME_RANK
16 SUBURB_TOWN_NAME_2016_ADJUSTED_CRIME_RANK_PERCENTILE
17 ADJUSTED_CRIME_RANK_SCALE
18 SUBURB_MOST_INT_STUDENT_LANG
19 INT_STUDENT_POPULATION_ARRIVAL_ALL_YEARS
20 TOTAL_INT_STUDENTS_PER_SUBURB
21 TOTAL_INT_STUDENT_PER_LANGUAGE
22 TMP_INT_STUDENT_NATIVE_LANG
23 TMP_SUBURB_STUDENT_POPULATION_SCALE_RANK
24 Acholi
25 African Languages, nec
26 African Languages, nfd
27 Afrikaans
28 Akan
29 Albanian
30 Amharic
31 Anuak
32 Arabic
33 Armenian
34 Assyrian Neo-Aramaic
35 Bengali
36 Bisaya
37 Bosnian
38 Bulgarian
39 Burmese
40 Burmese and Related Languages, nec
41 Burmese and Related Languages, nfd
42 Cantonese
43 Catalan
44 Cebuano
45 Chaldean Neo-Aramaic
46 Chin Haka
47 Chinese, nfd
48 Creole, nfd
49 Croatian
50 Czech
51 Danish
52 Dari
53 Dhivehi
54 Dinka
55 Dravidian, nec
56 Dutch
57 English
58 Estonian
59 Fijian
60 Filipino
61 Finnish
62 French
63 French Creole, nfd
64 German
65 Greek
66 Gujarati
67 Hakka
68 Harari
69 Hausa
70 Hazaraghi
71 Hebrew
72 Hindi
73 Hungarian
74 Iban
75 Igbo
76 Ilonggo (Hiligaynon)
77 Inadequately described
78 Indonesian
79 Iranic, nfd
80 Italian
81 Japanese
82 Kannada
83 Karen
84 Khmer
85 Kinyarwanda (Rwanda)
86 Kirundi (Rundi)
87 Konkani
88 Korean
89 Kurdish
90 Lao
91 Lithuanian
92 Loma (Lorma)
93 Luganda
94 Macedonian
95 Malay
96 Malayalam
97 Maltese
98 Mandarin
99 Maori (Cook Island)
100 Maori (New Zealand)
101 Marathi
102 Mauritian Creole
103 Min Nan
104 Mongolian
105 Nepali
106 No international students recorded as living in this area.
107 Norwegian
108 Not stated
109 Nuer
110 Nyanja (Chichewa)
111 Oriya
112 Oromo
113 Other Southern Asian Languages
114 Pashto
115 Persian (excluding Dari)
116 Pidgin, nfd
117 Polish
118 Portuguese
119 Punjabi
120 Rohingya
121 Romanian
122 Russian
123 Samoan
124 Serbian
125 Shilluk
126 Shona
127 Sindhi
128 Sinhalese
129 Slovak
130 Slovene
131 Somali
132 Southern Asian Languages, nfd
133 Spanish
134 Swahili
135 Swedish
136 Tagalog
137 Tamil
138 Telugu
139 Tetum
140 Thai
141 Tibetan
142 Tigrinya
143 Tok Pisin (Neomelanesian)
144 Tongan
145 Tswana
146 Turkish
147 Tuvaluan
148 Ukrainian
149 Urdu
150 Vietnamese
151 Wu
152 Yoruba
153 Zomi
'''
with open('FINAL_SUBURB_ANALYSIS.csv', 'rb') as csvfile:
	readr = csv.reader(csvfile, delimiter=',')
	initial = readr.next()
	for line in readr:
		print json.dumps(row_to_obj(line))
	# print initial
	# for row in readr:
	# 	print ', '.join(row)