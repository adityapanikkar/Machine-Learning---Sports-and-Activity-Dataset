#COde to aggregate all the data from activities and people. This averages each segment by doing 125/5
#giving 60 readings per person per activity
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

pathlist=[]
activities=19
people=8
columns=45
final = []
for a in range(1,activities+1):
  for b in range(1,people+1):

        if(1<=a<=9):
            activity='0'+str(a)
        else:
            activity=str(a)
        activity='a'+activity
        person='p'+str(b)
        data_path=activity+'/'+person+'/'
        pathlist.append(data_path)
        print('pathlist created')

data_home = "C:/Users/Aditya/Desktop/data/"
for d in pathlist:


    user_data = d
    num_of_segments = 60

    big = []
    # load data for a single user that is walking in a parking lot
    file_names = load_segment_names(data_home, user_data)
    for z in range(num_of_segments):
        walk_file = data_home + user_data + file_names[z]
        df = pd.read_csv(walk_file, names=feat_names)
        # print(generate_feature_names())
        # print(file_names)
        woo = []
        for i in range(columns):
            sum = 0
            for j in range(125):
                # print(j,'->',df.iloc[j][i])
                sum = sum + df.iloc[j][i]
            sum = sum / 125
            file1 = open("C:/Users/Aditya/Desktop/data/MyFile.txt", "a+")
            if(i<columns-1):
                file1.write(str(sum) + ',')

            else:
                file1.write(str(sum) + ',' + '\n')
            file1.close()
