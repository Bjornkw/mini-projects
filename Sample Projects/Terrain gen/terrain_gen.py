# -*- coding: utf-8 -*-
"""
Procedural terrain generator
Simulating hydrodynamic erosion

UNFINISHED!

Created on Wed Mar  2 20:28:14 2022

@author: Björn Krook Willen
"""

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

## FUNCTIONS

def GetGradient(image):
    
    x_kernel=np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])/2
    y_kernel=np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])/2
    
    img_bw=cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    img_blur=cv.GaussianBlur(img_bw,(5,5),0)
    
    x_grad=cv.filter2D(img_blur, cv.CV_32F, x_kernel)
    y_grad=cv.filter2D(img_blur, cv.CV_32F, y_kernel)
    
    return [x_grad, y_grad]

def SimulateDrop(img, length):
    
    size_x=np.size(img,0)
    size_y=np.size(img,1)
    [x_grad, y_grad]=GetGradient(img)
    
    pos=np.array([size_x*np.random.random(), size_y*np.random.random()])
    path=np.zeros([length,2])
    
    for i in range(length):
        d_pos=np.array([x_grad[int(pos[1]),int(pos[0])], y_grad[int(pos[1]), int(pos[0])]])
        pos=pos-d_pos*5
        path[i,0]=pos[0]
        path[i,1]=pos[1]
    
    return path

def UpdateImage(image, path):
    
    return 0

## MAIN

img=cv.imread('octaves.png')
path=SimulateDrop(img,500)
plt.imshow(img)
plt.plot(path[:,0],path[:,1],'r')
plt.plot(path[-1,0],path[-1,1],'*')