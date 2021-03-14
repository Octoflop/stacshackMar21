"""
    All of the comments are going to be string literals
    Dont @me
"""
import numpy as np
import pandas as pd
import cv2
import os
import sys
import csv

'// Transforms images to a standard format'
def transform(path) :
    im = cv2.imread(path, 1)
    im_small = cv2.resize(im, (150,150))
    im_gray = cv2.cvtColor(im_small, cv2.COLOR_RGB2GRAY)
    output = im_gray.flatten().tolist()
    return output

'// Runs the transformation on each file in a folder'
def transform_all():
    image_files = os.listdir(sys.argv[1])
    big_list = [] 
    for im in image_files:
        current = transform(os.path.join(sys.argv[1], im))
        current.append(int(sys.argv[2]))
        big_list.append(current)
    with open(sys.argv[3], 'w') as out_csv:
        writer = csv.writer(out_csv)
        writer.writerows(big_list)

transform_all()

    
