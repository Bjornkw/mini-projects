# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 01:29:10 2022

@author: Björn
"""

import taichi as ti
import numpy as np
ti.init(arch=ti.gpu)

win_size = [800, 800]
pixels_tmp = ti.field(dtype=float, shape=(win_size[0], win_size[1]))
pixels = ti.field(dtype=float, shape=(win_size[0], win_size[1]))

@ti.kernel
def FillRand():
    center = [int(win_size[0]/2), int(win_size[1]/2)]
    for i, j in pixels:
        if ( (i-center[0])**2 + (j-center[1])**2 ) < 10000:
            r = ti.random(ti.f32)
            if r < 0.5:
                pixels[i,j] = 1
            
@ti.kernel
def Iterate():
    for i, j in pixels:
        s = pixels[i,j]
        n = pixels[i,j+1]+pixels[i,j-1]+pixels[i+1,j]+pixels[i-1,j]+pixels[i+1,j+1]+pixels[i-1,j+1]+pixels[i+1,j-1]+pixels[i-1,j-1]
        
        if s == 1:
            if n < 2:
                pixels_tmp[i,j] = 0
            if n > 3:
                pixels_tmp[i,j] = 0
                
        if s == 0:
            if n ==3:
                pixels_tmp[i,j] = 1
                
@ti.kernel
def Copy():
    for i,j in pixels_tmp:
        pixels[i,j]=pixels_tmp[i,j]
    
FillRand()

gui = ti.GUI("Game of life", res=(win_size[0], win_size[1]))
while gui.running:
    Iterate()
    Copy()
    gui.set_image(pixels)
    gui.show()