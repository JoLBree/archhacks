import pandas as pd
import json
import unicodecsv as csv

with open('round1/distances.json') as data_file:    
    round1 = json.load(data_file)
    
with open('round2/distances.json') as data_file:    
    round2 = json.load(data_file)

all_schools = round1 + round2

keys = all_schools[0].keys()
with open('bus_info.csv', 'wb') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(all_schools)
