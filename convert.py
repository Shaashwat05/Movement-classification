import os
import glob

for path in glob.glob('/home/shaashwatlobnikki/Desktop/pose_classification/data/*/'):
    for bvh in glob.glob(path+'*.bvh'):
        os.system("bvh-converter "+ bvh)