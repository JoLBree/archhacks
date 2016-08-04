# number of applicants per school
import pandas as pd
import json

def calc_num_applicants(applications_csv, bus_csv):
    applications_df = pd.read_csv(applications_csv)
    applications_df.columns = ['sch1','sch2']
    
    bus_df = pd.read_csv(bus_csv)
    bus_df['application_count'] = 0
    
    for school in applications_df['sch1']:
        if school != "Other":
            bus_df.loc[bus_df['school']==school,'application_count'] += 1
    
    for school in applications_df['sch2']:
        if school != 'N/A':
            bus_df.loc[bus_df['school']==school,'application_count'] += 1
        
    bus_df.to_csv('bus_info2.csv', index=False)
    print "done"

calc_num_applicants("ArchHacks Applications for buses 2 standardized.csv", "bus_info.csv")