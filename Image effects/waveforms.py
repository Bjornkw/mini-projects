# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 19:13:50 2023

@author: bjorn
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

XRES = 32
YRES = 2500

def noise_bands(image):
    pass

def sine_bands(image):
    pass

def noise_spiral(image):
    pass

def sine_spiral(image):
    pass

img = cv2.imread("eye.png")
W = img.shape[0]
H = img.shape[1]
img = cv2.blur(img, (12,12), cv2.BORDER_DEFAULT)
img = np.array(img, dtype = float)
img_bw = (img[:,:,0]+img[:,:,1]+img[:,:,2])/(255*3)
img = cv2.resize(img_bw, (YRES,XRES))

plt.figure(figsize=(10, 10*(W/H)), dpi=200)
plt.axis('off')
x = np.linspace(0,1,YRES)
for i in range(XRES):
    y = ((np.random.random(YRES)-0.5)*(1-img[i,:]))-i
    plt.plot(x,y, "black", lw=0.4)