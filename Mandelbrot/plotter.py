# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 03:08:10 2022

@author: Björn
"""

import numpy as np
from numpy import genfromtxt
import matplotlib.pyplot as plt

image = genfromtxt('img.csv', delimiter=',', dtype=np.float64)
img = image
img = np.mod(img,32)
img = img.transpose()


plt.figure(dpi=600)
fig = plt.imshow(img, cmap="twilight")
plt.axis('off')
#fig.axes.get_xaxis().set_visible(False)
#fig.axes.get_yaxis().set_visible(False)