import os
import glob
import pandas as pd 
import numpy as np

for path in glob.glob('/home/shaashwatlobnikki/Desktop/pose_classification/data/*/'):
    for bvh in glob.glob(path+'*.bvh'):
        os.system("bvh-converter "+ bvh)


for path in glob.glob('/home/shaashwatlobnikki/Desktop/pose_classification/data_csv/*csv'):
    
    dat = pd.read_csv(path)
    dat = dat.drop(['Time'], axis=1)

    coors = []
    coors_final = []

    for col in dat.columns:
        if col.endswith('.Z'):
            continue
        else:
            coors.append(dat[col].values.tolist())

    for i in range(len(coors[0])):
        coord = []
        for j in range(len(coors)//2):
            coord.append([coors[j*2][i], coors[j*2+1][i]])
        coors_final.append(coord)

    