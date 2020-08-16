import pickle
import cv2
import numpy as np

pickle_in = open("pickle_data/02_10_worldpos.pickle","rb")
exer = pickle.load(pickle_in)



ind = [26, 27, 28, 32, 33, 34, 4, 5, 6, 13, 14, 15, 23]

pairs = [[0,1], [1,2], [7,8], [8,9], [10,11], [11,12], [3,4], [4,5], [0,3], [7,10], [3,10], [0,7] ]

img = np.zeros((480,640))

exer = np.array(exer)*15

exer = exer.tolist()

for i in range(len(exer)):
    for j in range(len(exer[0])):
        exer[i][j][0]+=200
        exer[i][j][1] = 550 - exer[i][j][1]

print(len(exer[0]))

for i in range(len(exer)):

    for j in range(13):
        cv2.circle(img, (int(exer[i][j][0]), int(exer[i][j][1])), 5, (255, 255, 255), -1)
    for j in pairs:
        cv2.line(img, tuple(exer[i][j[0]]), tuple(exer[i][j[1]]), (255, 255, 255), 3)
    cv2.imshow("img", img)
    cv2.waitKey(1)
    img = np.zeros((480,640))
