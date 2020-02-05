# Reads a csv file and adds the headers and stores as a new csv file

import numpy as np
import pandas as pd
import os


def generate_feature_names():
    '''Creates feature names for dataframe header'''
    feat_names = []
    for unit_label in ["T", "RA", "LA", "RL", "LL"]:
        for sensor  in ["acc","gyro","mag"]:
            for position in ['X','Y','Z']:
                feat_names.append(unit_label + "_" + position + sensor)
    return feat_names

def load_segment_names(home, data):
    '''Loads activity data for a specificed subset'''
    return [filename for filename in os.listdir(home + data)]

feat_names = generate_feature_names()
dflist=[]
data_home = "C:/Users/Aditya/Desktop/data/"

final=[]
walk_file = "C:/Users/Aditya/Desktop/data/MyFile.csv"

df = pd.read_csv(walk_file,names=feat_names)
plist=['a1','a2','a3','a4','a5','a6','a7','a8','a9','a10','a11','a12','a13','a14','a15','a16','a17','a18','a19']
activities=len(plist)
for x in range(activities):
    for y in range(480):
            final.append(plist[x])
#print(len(final))

df=df.assign(Activity=final)
#print(df)
df.to_csv("C:/Users/Aditya/Desktop/pot.csv")