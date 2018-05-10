python csv_to_json.py > suburbs.json
mongoimport --drop --username admin --password AnVkgeYGpDV6RaQ8y1duvdh+dD/E4z+dh46MUaU/DkA= --db sheltr --collection suburbs < suburbs.json

#python3 uni_csv_to_json.py > universities.json
#mongoimport --drop --username admin --password AnVkgeYGpDV6RaQ8y1duvdh+dD/E4z+dh46MUaU/DkA= --db sheltr --collection universities < universities.json

#python lang_csv_to_json.py > languages.json
#mongoimport --drop --username admin --password AnVkgeYGpDV6RaQ8y1duvdh+dD/E4z+dh46MUaU/DkA= --db sheltr --collection languages < languages.json
