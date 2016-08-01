# Get city, state
import json
import requests

def find_city(address_components):
    for component in address_components:
        if 'locality' in component['types']:
            return component['long_name']
    for component in address_components:
        if 'country' in component['types']:
            return component['long_name']
        
def find_state(address_components):
    for component in address_components:
        if 'administrative_area_level_1' in component['types']:
            return component['short_name']

with open('consensus.json') as data_file:    
    consensus = json.load(data_file)
    
manual2 = []    

for entry in consensus:
    r = requests.get("https://maps.googleapis.com/maps/api/geocode/json?address="+entry['address']+"")
#     print r.text
    print "requesting..."
    data = r.json()
#         data = json.loads(r'{"results":[{"address_components":[{"long_name":"124","short_name":"124","types":["street_number"]},{"long_name":"Raymond Avenue","short_name":"Raymond Ave","types":["route"]},{"long_name":"Poughkeepsie","short_name":"Poughkeepsie","types":["locality","political"]},{"long_name":"Poughkeepsie","short_name":"Poughkeepsie","types":["administrative_area_level_3","political"]},{"long_name":"Dutchess County","short_name":"Dutchess County","types":["administrative_area_level_2","political"]},{"long_name":"New York","short_name":"NY","types":["administrative_area_level_1","political"]},{"long_name":"United States","short_name":"US","types":["country","political"]},{"long_name":"12604","short_name":"12604","types":["postal_code"]}],"formatted_address":"124 Raymond Ave, Poughkeepsie, NY 12604, USA","geometry":{"location":{"lat":41.68652669999999,"lng":-73.8981091},"location_type":"ROOFTOP","viewport":{"northeast":{"lat":41.6878756802915,"lng":-73.89676011970849},"southwest":{"lat":41.6851777197085,"lng":-73.89945808029151}}},"place_id":"ChIJ60l4A1c-3YkRV2-BRF2VaEY","types":["street_address"]}],"status":"OK"}')
    if data['status'] == 'OK':
        entry['city,state'] = find_city(data['results'][0]['address_components'])+", "+find_state(data['results'][0]['address_components'])
    else:
        print data['status']
        manual2.append(entry['school'])

print consensus
print manual2

with open('cities_states_consensus.json', 'w') as fp:
        json.dump(consensus, fp)

with open('cities_states_manual.json', 'w') as fp:
        json.dump(manual2, fp)
print "done"