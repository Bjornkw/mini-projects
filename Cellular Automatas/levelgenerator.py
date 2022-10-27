# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 01:10:11 2022

@author: Björn
"""

import numpy as np
import autorule
import caves

###############################################################################

class Level():
    def __init__(self, size = [256, 256], rule = 67, noise_level=0.55):
        self.size = size
        self.rule = 67
        self.noise_level = noise_level
        
    def __str__(self):
        return "Filled"*('level' in dir(self)) + "Empty"*(not 'level' in dir(self)) + " Level Object"
        
    def generate_level(self, n=5):
        cavegen = caves.Canvas(self.size)
        cavegen.fill_noise(self.noise_level)
        cavegen.iterate(n)
        img = cavegen.canvas*(-1)+1
        step = 2
        img[step:self.size[1]] = 2*img[step:self.size[1]] + img[0:self.size[1]-step] - img[step:self.size[1]]*img[0:self.size[1]-step]
        img[0:step] = 2
        self.level = img
        self.level_mask = img>0
        self.generate_floor()
    
    def generate_floor(self):
        rule = autorule.Rule(2,1,self.size,self.rule)
        floor = rule.canvas
        self.level = self.level + floor*(self.level_mask*(-1)+1)*0.2+0.1

if __name__ == "__main__":
    import matplotlib.pyplot as plt
    level = Level([64, 64])
    level.generate_level(40)
    print(level)
    plt.figure(dpi=400)
    fig = plt.imshow(level.level, cmap='Greys')
    fig.axes.get_xaxis().set_visible(False)
    fig.axes.get_yaxis().set_visible(False)
