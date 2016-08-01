# get driving distance
import json
import requests

def is_within_driving_range(entry):
    cutoff_hours = 14
    if 'driving_time' in entry:
        if 'day' not in entry['driving_time']:
            time_components = entry['driving_time'].split(" ")
            if 'hours' not in time_components:
                return True
            else:
                hours = time_components[time_components.index('hours')-1]
                if int(hours) < cutoff_hours:
                    return True
    return False

with open('cities_states_consensus.json') as data_file:    
    cities_states = json.load(data_file)

# with open('cities_states_manual.json') as data_file:    
#     manual = json.load(data_file)

manual3 = []
    
# addresses = concat_addresses(cities_states)

# print addresses

for entry in cities_states:
    print "requesting..."
    r = requests.get("https://maps.googleapis.com/maps/api/distancematrix/json?origins="+entry['address']+"&destinations=1 Brookings Dr, St. Louis, MO 63130, United States")
#     print r.text
    data = r.json()
    if data['status'] == 'OK':
        if data['rows'][0]['elements'][0]['status']=='OK':
            entry['driving_time'] = data['rows'][0]['elements'][0]['duration']['text']
        else:
            print "no driving "+data['rows'][0]['elements'][0]['status']
        entry['within_driving_range'] = is_within_driving_range(entry)
    else:
        print data['status']
        manual3.append(entry['school'])

print cities_states
print manual3
# print no_distance


with open('distances.json', 'w') as fp:
        json.dump(cities_states, fp)

with open('distances_nodata.json', 'w') as fp:
        json.dump(manual3, fp)
print "done"