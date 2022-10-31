# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 23:38:46 2022

@author: Björn
"""

import numpy as np
import cv2 as cv
    
###############################################################################

class Canvas():
    def __init__(self, size, noise_level = 0.5):
        self.size = size
        self.fill_noise(noise_level)
    
    def fill_noise(self, noise_level):
        self.canvas = np.random.random([self.size[0], self.size[1]])
        
    def filter(self):
        img = self.canvas
        kernel = np.ones((5,5),np.float32)/25
        out = cv.filter2D(img,-1,kernel)
        return out
    
    def cube(self):
        self.canvas[44:84,44:84] = np.ones([40,40])*0.2
    
    def iterate(self, n):
        for s in range(n):
            canvas_tmp = self.filter()
            self.canvas = canvas_tmp
            
    def mask(self, cutoff):
        return self.canvas>cutoff

###############################################################################

if __name__ == "__main__":
    import matplotlib.pyplot as plt
    size = [128, 128]
    c = Canvas(size, 0.54)
    c.cube()
    c.iterate(12)
    img = c.mask(0.49)
    plt.figure(dpi=200)
    fig = plt.imshow(img, cmap='Greys')
    fig.axes.get_xaxis().set_visible(False)
    fig.axes.get_yaxis().set_visible(False)