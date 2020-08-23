import tensorflow as tf 
from tensorflow.keras.models import load_model
import pickle
import numpy as np 



model = load_model("weights-improvement-10-0.4311-biggeer.hdf5")

pickle_in = open('/home/shaashwatlobnikki/Desktop/movement_classification/pickle_data/02_07_worldpos.pickle',"rb")
data = pickle.load(pickle_in)

data = data[:150]
data = np.array(data)

print(data.shape)
data = np.reshape(data, (1, data.shape[0]*data.shape[1]*data.shape[2], 1))
print(data.shape)
print(data)

print(model.predict(data))

