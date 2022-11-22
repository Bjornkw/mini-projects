# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 03:08:10 2022

@author: Björn
"""

import taichi as ti
import numpy as np
from PIL import Image
from numpy import genfromtxt

cmap = genfromtxt('cmap.csv', delimiter=',')

ti.init(arch=ti.gpu)

win_size_s = [1920, 1080]
center = [-0.908445250432262, -0.2676926298264956]
pixels_s = ti.field(dtype=ti.float64, shape=(win_size_s[0], win_size_s[1]))
scale=0.0000236000184180249
itr_lim_s = 25000

###############################################################################

@ti.func
def complex_sqr_fancy(z: ti.float64):
    return ti.Vector([z[0]**2 - z[1]**2, z[1] * z[0] * 2])


@ti.kernel
def paint_fancy(s: ti.float64, c1: ti.float64, c2: ti.float64):
    for i, j in pixels_s:
        
        x_min = c1 - s
        x_max = c1 + s
        y_min = c2 - s*(win_size_s[1]/win_size_s[0])
        y_max = c2 + s*(win_size_s[1]/win_size_s[0])
        x = x_min + (x_max-x_min)*(i/win_size_s[0])
        y = y_min + (y_max-y_min)*(j/win_size_s[1])
        
        z = ti.Vector([0, 0], dt=ti.float64)
        c = ti.Vector([x, y], dt=ti.float64)
        
        itr = 0
        while z.norm() < 16 and itr < itr_lim_s:
            z = complex_sqr_fancy(z) + c
            itr += 1
            
        pixels_s[i, j] = itr

###############################################################################

def save_frame(d, q):
    print('Saving frame ' + str(saved_frames)+"/"+str(max_frames))
    paint_fancy(d[0], d[1], d[2])
    image = np.zeros((win_size_s[1], win_size_s[0], 3), dtype=np.uint8)
    itr = pixels_s.to_numpy(dtype=np.float64)
    itr_mod = np.mod(itr+q, 64)
    for i in range(win_size_s[1]):
        for j in range(win_size_s[0]):
            if itr[j, i] == itr_lim_s:
                image[i,j,:]=0
            else:
                image[i,j,0] = cmap[int(itr_mod[j,i])][0]*255.0
                image[i,j,1] = cmap[int(itr_mod[j,i])][1]*255.0
                image[i,j,2] = cmap[int(itr_mod[j,i])][2]*255.0
    image = Image.fromarray(image, 'RGB')
    name = "frame" + str(saved_frames) + ".png"
    image.save(name)

###############################################################################

if __name__=="__main__":
    i = 0
    saved_frames = 0
    max_frames=64
    for i in range(max_frames):
        saved_frames = i
        save_frame([scale, center[0], center[1]], i)
        i=i+1
    print('Done!')

    