[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

[![Python 3.8](https://img.shields.io/badge/python-3.8-green.svg)](https://www.python.org/downloads/release/python-380/) 

# Movement-classification
The aim of the project is to classify types of **Movements** instead of just single **Postures**. It is a combination of a lot of components and ideas put together.

### BVH file
 **BVH(BioVision Hierarchy)** is a file format used to define a skeleton structure and its connections. It is a **Motion capture** file which stores position/rotation of each joint per frame. The movements can be viewed directly by importing this file or also by imparting this movement to 3d Characters/Rig.
 
 ### CMU dataset
 The **Carnegie Mellon University** [dataset](https://sites.google.com/a/cgspeed.com/cgspeed/motion-capture/cmu-bvh-conversion) contains about 2500 BVH files accounting for various types of movements. Basic movements such as walking, running, jumping have many references and files. Some complex movements such as swordplay or cartwheel are also included in the dataset.


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





