import tensorflow as tf 
from tensorflow.keras.models import Sequential
from tensorflow.keras.callbacks import ModelCheckpoint
from tensorflow.keras.layers import Dense,MaxPooling1D,Softmax, LSTM, Dropout
from tensorflow.keras import utils
import numpy as np
import pickle
import glob
import pandas as pd

gpus = tf.config.experimental.list_physical_devices('GPU')
if gpus:
    try:
        # Restrict TensorFlow to only use the fourth GPU
        tf.config.experimental.set_visible_devices(gpus[0], 'GPU')

        # Currently, memory growth needs to be the same across GPUs
        for gpu in gpus:
            tf.config.experimental.set_memory_growth(gpu, True)
        logical_gpus = tf.config.experimental.list_logical_devices('GPU')
        print(len(gpus), "Physical GPUs,", len(logical_gpus), "Logical GPUs")
    except RuntimeError as e:
        # Memory growth must be set before GPUs have been initialized
        print(e)

x  = []
y = []
seq = []
seq_len = 100
    
info = pd.read_excel('cmu-mocap-index-spreadsheet.xls')
info = info.drop(['SUBJECT from CMU web database'], axis=1)

walk = info.loc[info['DESCRIPTION from CMU web database'] == 'walk']
walk = walk['MOTION'].values.tolist()
walk = walk[:6]

run = info.loc[info['DESCRIPTION from CMU web database'] == 'run']
run = run['MOTION'].values.tolist()
run = run[:6]

jump = info.loc[info['DESCRIPTION from CMU web database'] == 'jump']
jump = jump['MOTION'].values.tolist()
jump = jump[:6]

tot = walk + run + jump
print(jump)

for ex in tot:
    pickle_in = open('/home/shaashwatlobnikki/Desktop/movement_classification/pickle_data/'+ ex +'_worldpos.pickle',"rb")
    data = pickle.load(pickle_in)

    seq.append(data)
print(tot)

for fileno in range(len(seq)):
    #seq[fileno] = seq[fileno][:-(len(seq[fileno])%300)]
    for i in range(0,len(seq[fileno])-seq_len,1):
        x.append(seq[fileno][i:i+seq_len])
       
        if(tot[fileno] in walk):
            y.append(0)
        elif(tot[fileno] in run):
            y.append(1)
        else:
            y.append(2)

###   (4320,150,13,2) ---->>>   (4320, 150, 26)

X= np.asarray(x)
X = np.reshape(X, (X.shape[0], X.shape[1],X.shape[2]*X.shape[3]))
X= X/np.max(X)
print(X.shape)

y = utils.to_categorical(y)

#print(y.shape)
model = Sequential()
model.add(LSTM(256, input_shape = (X.shape[1], X.shape[2]), return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(256))
model.add(Dropout(0.2))
model.add(Dense(3, activation='softmax'))
model.compile(loss = 'categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

model.summary()

filepath = "weights-improvement-{epoch:02d}-{loss:.4f}-biggeer.hdf5"
checkpoint = ModelCheckpoint(filepath, monitor='loss', verbose = 1, save_best_only=True, mode = 'min')
callbacks_list = [checkpoint]

model.fit(X, y, epochs = 30, batch_size=32, callbacks=callbacks_list)











