import tensorflow as tf 
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,MaxPooling1D,Softmax
import numpy as np
import pickle
import glob
import pandas as pd

info = pd.read_excel('cmu-mocap-index-spreadsheet.xls')
#info = info.iloc[1:]
info = info.drop(['SUBJECT from CMU web database'], axis=1)

x  = []
y = []

walk = info.loc[info['DESCRIPTION from CMU web database'] == 'walk']
walk = walk['MOTION'].values.tolist()

run = info.loc[info['DESCRIPTION from CMU web database'] == 'run']
run = run['MOTION'].values.tolist()

jump = info.loc[info['DESCRIPTION from CMU web database'] == 'jump']
jump = jump['MOTION'].values.tolist()

tot = walk + run + jump
seq = []
seq_len = 300

for ex in tot:
    pickle_in = open('/home/shaashwatlobnikki/Desktop/pose_classification/pickle_data/'+ ex +'.pickle',"rb")
    data = pickle.load(pickle_in)

    seq.append(data)


for fileno in range(len(seq)):
    #seq[fileno] = seq[fileno][:-(len(seq[fileno])%300)]
    for i in range(0,len(seq[fileno])-seq_len,1):
        x.append(seq[fileno][i:i+seq_len])
        if(tot[fileno] in walk):
            y.append('walk')
        elif(tot[fileno] in run):
            y.append('run')
        else:
            y.append('jump')










