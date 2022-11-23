# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 00:23:11 2022

@author: Björn Krook Willén
"""

import taichi as ti
import numpy as np
from numpy import genfromtxt

cmap = genfromtxt('cmap.csv', delimiter=',')

ti.init(arch=ti.gpu)

win_size = [1400, 700]
center = [0.5, 0]
center_j = [-1.5, 0]
pixels = ti.field(dtype=float, shape=(win_size[0], win_size[1]))
scale=1.9
scale_j = 3
itr_lim = 2500

###############################################################################

@ti.func
def complex_sqr(z: float):
    return ti.Vector([z[0]**2 - z[1]**2, z[1] * z[0] * 2])

@ti.kernel
def paint(s: float, c1: float, c2: float, s2: float, c3: float, c4: float, p1: float, p2: float):
    for i, j in pixels:
        
        if i<int(win_size[0]/2):
            x_min = c1 - s
            x_max = c1 + s
            y_min = c2 - s*(win_size[1]/win_size[0])
            y_max = c2 + s*(win_size[1]/win_size[0])
            x = x_min + (x_max-x_min)*(i/win_size[0])
            y = y_min + (y_max-y_min)*(j/win_size[1])
        
            z = ti.Vector([0, 0], dt=float)
            c = ti.Vector([x, y], dt=float)
        
            itr = 0
            while z.norm() < 8 and itr < itr_lim:
                z = complex_sqr(z) + c
                itr += 1
            
            pixels[i, j] = 1 - ti.sqrt(ti.sqrt(itr/itr_lim))
        else:
            x_min = c3 - s2
            x_max = c3 + s2
            y_min = c4 - s2*(win_size[1]/win_size[0])
            y_max = c4 + s2*(win_size[1]/win_size[0])
            x = x_min + (x_max-x_min)*(i/win_size[0])
            y = y_min + (y_max-y_min)*(j/win_size[1])
        
            z = ti.Vector([x, y], dt=float)
            c = ti.Vector([p1, p2], dt=float)
        
            itr = 0
            while z.norm() < 8 and itr < itr_lim:
                z = complex_sqr(z) + c
                itr += 1
            
            pixels[i, j] = 1 - ti.sqrt(ti.sqrt(itr/itr_lim))
            
def scr2z(i, j):
    x_min = center[0] - scale
    x_max = center[0] + scale
    y_min = center[1] - scale*(win_size[1]/win_size[0])
    y_max = center[1] + scale*(win_size[1]/win_size[0])
    x = x_min + (x_max-x_min)*i
    y = y_min + (y_max-y_min)*j
    return x, y

###############################################################################

if __name__=="__main__":
    pos = np.array([[0.5,0.5]])
    idx = np.random.randint(0, 1, size=(1,))
    gui = ti.GUI("Mandelbrot fractal and corresponding julia fractals", res=(win_size[0], win_size[1]))
    while gui.running:
        p1, p2 = scr2z(pos[0,0], pos[0,1])
        paint(scale, center[0], center[1], scale_j, center_j[0], center_j[1], p1, p2)
        gui.set_image(pixels)
        gui.circles(pos, radius=5, palette=[0x068587, 0xED553B, 0xEEEEF0], palette_indices=idx)
        gui.show()

        if gui.get_event(ti.GUI.PRESS):
            if gui.event.key == "LMB":
                mouse_x, mouse_y = gui.get_cursor_pos()
                pos[0,0] = mouse_x
                pos[0,1] = mouse_y 
