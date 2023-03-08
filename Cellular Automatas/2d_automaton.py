# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 22:10:05 2023

@author: bjorn
"""

import taichi as ti
import numpy as np
import time
ti.init(arch=ti.gpu)

win_size = [800, 800]
display = ti.field(dtype=float, shape=(win_size[0], win_size[1],3))
alive = ti.field(dtype=int, shape=(win_size[0], win_size[1]))
alive_tmp = alive = ti.field(dtype=int, shape=(win_size[0], win_size[1]))
age = ti.field(dtype=int, shape=(win_size[0], win_size[1]))
poison = ti.field(dtype=float, shape=(win_size[0], win_size[1]))

###############################################################################

@ti.kernel
def FillRand():
    center = [int(win_size[0]/2), int(win_size[1]/2)]
    for i, j in alive:
        if ( (i-center[0])**2 + (j-center[1])**2 ) < 5000:
            r = ti.random(ti.f32)
            if r < 0.5:
                alive[i,j] = 1
            
@ti.kernel
def Automaton():
    center = [int(win_size[0]/2), int(win_size[1]/2)]
    for i, j in alive:
        s = alive[i,j]
        n = alive[i,j+1]+alive[i,j-1]+alive[i+1,j]+alive[i-1,j]+alive[i+1,j+1]+alive[i-1,j+1]+alive[i+1,j-1]+alive[i-1,j-1]
        poison[i, j] = poison[i, j]*0.99
        if s == 1:
            poison[i, j] = poison[i, j] + n
            age[i, j] = age[i, j] + 1
            if n < 2:
                alive_tmp[i,j] = 0
                age[i, j] = 0
            if n > 9:
                alive_tmp[i,j] = 0
                age[i, j] = 0
        if s == 0 and poison[i, j]<50:
            if n ==3:
                alive_tmp[i,j] = 1
                
        if age[i, j] > np.random.rand()*500:
            alive_tmp[i, j] = 0
            age[i, j] = 0
            
        if poison[i, j] > 100+np.random.rand()*1000:
            alive_tmp[i, j] = 0
            age[i, j] = 0

@ti.kernel
def Draw():
    for i,j in alive_tmp:
        alive[i,j] = alive_tmp[i,j]
        display[i, j, 0] = age[i, j]*0.01
        
###############################################################################

    
FillRand()
gui = ti.GUI("Game of life", res=(win_size[0], win_size[1]))

while gui.running:
    Automaton()
    Draw()
    gui.set_image(display)
    gui.show()