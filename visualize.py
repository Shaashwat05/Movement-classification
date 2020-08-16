import pickle
import cv2
import numpy as np

pickle_in = open("pickle_data/01_01_worldpos.pickle","rb")
exer = pickle.load(pickle_in)

pairs = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [0, 6], [6, 7], [7, 8], [8, 9], [9, 10], [0, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [13, 24], [24, 25], [25, 26], [26, 27], [27, 28], [13, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22]]

ind = [26, 27, 28, 32, 33, 34, 4, 5, 6, 13, 14, 15, 23]

fin_exer = []

for i in range(len(exer)):
    coor = []
    for j in range(len(exer[0])):
        if(j in ind):
            coor.append(exer[i][j])
    
    fin_exer.append(coor)



