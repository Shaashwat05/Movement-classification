import tensorflow as tf 
from tensorflow.keras.models import load_model
import pickle
import numpy as np 

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

model = load_model("weights-improvement-10-0.4311-biggeer.hdf5", compile=False)

pickle_in = open('/home/shaashwatlobnikki/Desktop/movement_classification/pickle_data/09_03_worldpos.pickle',"rb")
data = pickle.load(pickle_in)

data = data[:150]
data = np.array(data)


data = np.reshape(data, (1, data.shape[0]*data.shape[1]*data.shape[2], 1))


print(model.predict_classes(data))

