import tensorflow as tf
import matplotlib.pyplot as plt
import math
import cv2
import numpy as np
from tensorflow.keras.models import load_model


model = load_model("weights-improvement-17-0.0000-biggeer.hdf5")


def imgprep(img):
    img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    a=np.uint8(np.zeros((img.shape[1],img.shape[1],3)))
    a[:img.shape[0],:,:]=img[:,:,:]
    img=cv2.resize(a, (257,257))
    img=np.copy(img)
    img=np.reshape(img,(1,257,257,3))
    img=np.float32(img)
    return (img-127.5)/127.5

def poseproc(img):
    a=interpreter.set_tensor(input_details[0]['index'],img)
    interpreter.invoke()
    hm=interpreter.get_tensor(output_details[0]['index'])
    ofs=interpreter.get_tensor(output_details[1]['index'])
    hm = 1/(1 + np.exp(-hm))
    hm=np.reshape(hm, (9,9,17))
    ofs=np.reshape(ofs, (9,9,34))
    kp=list()
    poq=list()
    for i in range(17):
        q, w= np.unravel_index(hm[:,:,i].argmax(), hm[:,:,i].shape)
        poq.append(hm[q,w,i])
        e= ofs[q, w, i]
        r= ofs[q, w, i+17]
        kp.append([r+((w/8.0)*256), e+((q/8.0)*256)])
    kp=np.array(kp)
    kp=np.uint32(np.round(kp))
    return kp, poq


interpreter = tf.lite.Interpreter(model_path="posenet257.tflite")
interpreter.allocate_tensors()
input_details=interpreter.get_input_details()
output_details=interpreter.get_output_details()

poses = []

cap=cv2.VideoCapture(0)
while True:
    ret, frame=cap.read()
    if not ret:
        break
    frame1=imgprep(frame)
    dots, jk=poseproc(frame1)
    poses.append(dots)
    frame1=frame1*127.5+127.5
    thresh=0.03
    frame1=np.uint8(cv2.cvtColor(frame1.reshape((257,257,3)), cv2.COLOR_BGR2RGB))
    if(len(poses)>100):
        mvmt = model.predict(poses[-100:-1].reshape(len(poses), len(poses[0])*len(poses[0][0])))
        print(mvmt)
        
    
    cv2.imshow("im",cv2.resize(frame1,(512,512)))
    if cv2.waitKey(40) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()