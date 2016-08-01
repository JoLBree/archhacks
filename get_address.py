import pandas as pd
import requests
import json

invalid = ['N/A']

def get_school_address_set(path_to_csv):
    dataframe = pd.read_csv(path_to_csv)
    dataframe.columns = ['sch1','sch2']
    dataframe.ix[dataframe.sch1 == "Other",'sch1'] =dataframe.sch2 # merge the two columns
    school_list = dataframe['sch1'].dropna().tolist()
    
    with open('examined_schools.json') as data_file:    
        examined_schools = json.load(data_file)
    
    with open('old_overflow.json') as data_file:    
        old_overflow_schools = json.load(data_file)
    
    
    
#     print examined_schools
#     print old_overflow_schools
    
    schools = (set(school_list) - set(examined_schools)) |  set(old_overflow_schools)
    
    print schools

    consensus_locations = []
    manual_locations = []
    overflow_schools = []
    num_manual = 0
    
    google_api_max = 90
    
    for school in schools:
        print "requesting..."
        if school not in invalid:
            if google_api_max > 0:
                google_api_max -= 1
                r = requests.get("https://maps.googleapis.com/maps/api/place/textsearch/json?", params={"query":school,"key":""})
                data = r.json()
                if data['status'] == 'OVER_QUERY_LIMIT':
                    print data['status']
                    raise ValueError('Over query limit')
                else:
                    if data['status'] == 'OK' and len(data['results']) == 1:
                        consensus_locations.append({'school':school,'address':data['results'][0]['formatted_address']})
                    else:
                        manual_locations.append(school)
                        num_manual += 1
            else:
                overflow_schools.append(school)
    if google_api_max <= 0:
        print "API limit reached. Overflow schools are in overflow_schools"
    
    print consensus_locations
    print manual_locations
    print overflow_schools

    with open('consensus.json', 'w') as fp:
        json.dump(consensus_locations, fp)

    with open('overflow.json', 'w') as fp:
        json.dump(overflow_schools, fp)
        
    with open('manual.json', 'w') as fp:
        json.dump(manual_locations, fp)
        
    with open('schools_this_round.json', 'w') as fp:
        json.dump(schools, fp)

get_school_address_set("ArchHacks Applications for buses 2 standardized.csv")
print "done"