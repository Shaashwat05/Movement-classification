import tensorflow as tf 
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,MaxPooling1D,Softmax, LSTM, Dropout
from tensorflow.keras import utils
import numpy as np
import pickle
import glob
import pandas as pd

gpus = tf.config.experimental.get_visible_devices("GPU")
for gpu in gpus:
    tf.config.experimental.set_memory_growth(gpu,True)

x  = []
y = []
tot = walk + run + jump
seq = []
seq_len = 150
    
info = pd.read_excel('cmu-mocap-index-spreadsheet.xls')
info = info.drop(['SUBJECT from CMU web database'], axis=1)

walk = info.loc[info['DESCRIPTION from CMU web database'] == 'walk']
walk = walk['MOTION'].values.tolist()

run = info.loc[info['DESCRIPTION from CMU web database'] == 'run']
run = run['MOTION'].values.tolist()

jump = info.loc[info['DESCRIPTION from CMU web database'] == 'jump']
jump = jump['MOTION'].values.tolist()


for ex in tot:
    pickle_in = open('/home/shaashwatlobnikki/Desktop/movement_classification/pickle_data/'+ ex +'_worldpos.pickle',"rb")
    data = pickle.load(pickle_in)

    seq.append(data)


for fileno in range(len(seq)):
    #seq[fileno] = seq[fileno][:-(len(seq[fileno])%300)]
    for i in range(0,len(seq[fileno])-seq_len,1):
        x.append(seq[fileno][i:i+seq_len])
       
        if(tot[fileno] in walk):
            y.append(1)
        elif(tot[fileno] in run):
            y.append(2)
        else:
            y.append(3)

X= np.array(x)
X = np.reshape(X, (X.shape[0], X.shape[1]*X.shape[2]*X.shape[3]))
print(X.shape)

y = utils.to_categorical(y)

print(y.shape)

model = Sequential()
model.add(LSTM(256, input_shape = (X.shape[0], X.shape[1]), return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(256))
model.add(Dropout(0.2))
model.add(Dense(y.shape[1], activation='softmax'))
model.compile(loss = 'categorical_crossentropy', optimizer='adam')

filepath = "weights/weights-improvement-{epoch:02d}-{loss:.4f}-biggeer.hdf5"
checkpoint = ModelCheckpoint(filepath, monitor='loss', verbose = 1, save_best_only=True, mode = 'min')
callbacks_list = [checkpoint]

model.fit(X, y, epochs = 50, batch_size=64, callbacks=callbacks_list)











