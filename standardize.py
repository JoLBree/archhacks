import pandas as pd

sch1 = 'What school do you attend?'
sch2 = 'If you selected Other, what school do you attend?'
substitutions = {'Harvard University':['Harvard College','Harvard'],
                 'Drexel University':['Drexel'],
                 'Washington University in St. Louis':['Washington University in St. Louis School of Medicine','Launchcode - JAVA WUSM Campus'],
                 'Boston University':['boston university'],
                 'Union County College':['Union county college'],
                 "University of Maryland College Park":["University of Maryland",'University of Maryland - College Park'],
                 "Benha university - Shoubra":["Benha university - shoubra",'Shoubra Faculty of Engineering'],
                 "University of Colorado Boulder":["University of Colorado"],
                 'Illinois Institute of Technology ':['Illinois Institute of Technology, Chicago','Illinois Institute of Technology chicago','Illinois Institute Of Technology'],
                 'UC Berkeley':['University of California, Berkeley','Technical University of Munich, Germany (but in fall I will be a visiting researcher at UC Berkeley)'],
                 'N/A':['nan','n/A','n/a','N/a','na','NA','none','None','NONE','null','xxsxs','School of Hard Knocks']
                }


def standardize_csv(path_to_csv, substitutions):
    dataframe = pd.read_csv(path_to_csv)
    for school in substitutions:
        dataframe.loc[dataframe[sch2].isin(substitutions[school]),sch2] = school
    dataframe.to_csv('ArchHacks Applications for buses 2 standardized.csv', index=False)
    print "done"

standardize_csv("ArchHacks Applications for buses 2.csv", substitutions)