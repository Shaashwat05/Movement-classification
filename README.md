[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

[![Python 3.8](https://img.shields.io/badge/python-3.8-green.svg)](https://www.python.org/downloads/release/python-380/) 

# Movement-classification
The aim of the project is to classify types of **Movements** instead of just single **Postures**. It is a combination of a lot of components and ideas put together.

### BVH file
 **BVH(BioVision Hierarchy)** is a file format used to define a skeleton structure and its connections. It is a **Motion capture** file which stores position/rotation of each joint per frame. The movements can be viewed directly by importing this file or also by imparting this movement to 3d Characters/Rig. You can see the an example of the structure defination of the file below.
 
 #### Example
![Watch the video](https://github.com/Shaashwat05/Movement-classification/blob/master/images/bvh1.jpg)
 
 ### CMU dataset
 The **Carnegie Mellon University** [dataset](https://sites.google.com/a/cgspeed.com/cgspeed/motion-capture/cmu-bvh-conversion) contains about 2500 BVH files accounting for various types of movements. Basic movements such as walking, running, jumping have many references and files. Some complex movements such as swordplay or cartwheel are also included in the dataset.
 
 ### Visualization
 The visualization of the CMU dataset is done using **OpenCV**. By running visulaize.py you can see the output in the OpenCV window.This example show below is somewhat slower than the actual fps of the data. It can be changed esily in the code.
 
 ![Watch the gif](https://github.com/Shaashwat05/Movement-classification/blob/master/images/viz.gif)
 
 
 
 ### Pose Estimation
 The aim of the project is to identify and classify movements in live feed. The [**tflite model**](https://storage.googleapis.com/download.tensorflow.org/models/tflite/posenet_mobilenet_v1_100_257x257_multi_kpt_stripped.tflite) is used as the pose estimation AI. It gives **17 keypoints** in the body. It takes very less computation and is easy to work with.

### Model
I have used **Tensorflow** to train the dataset. A **Dense LSTM** model is used since the data is sequential. It is a time series data of about 120 frames per second and fits perfectly to LSTMs. The current version is being trained on jumping, running and walking with an input shape of (150,26). The output is a **Softmax** layer with categorical output. To summarize, the task is a **time series classification** task trained similar to most NLP models.

## Prerequisites

What things you need to install the software and how to install them

```
pickle
numpy
tensorflow==2.2
cv2
glob
pandas
os
```

## Getting Started

Download a python interpeter preferable a version beyond 3.0. Install the prerequisute libraries given above.

```
$tconvert.py

$train.py

$predict.py    

$visualize.py
```

## Built With

* [python](https://www.python.org/) - The software used
## Author
[![LinkedIn-profile](https://img.shields.io/badge/LinkedIn-Profile-teal.svg)](https://www.linkedin.com/in/shaashwat-agrawal-1904a117a/)

* [**Shaashwat Agrawal**](https://github.com/Shaashwat05) Authors 





