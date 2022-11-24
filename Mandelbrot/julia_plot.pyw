# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 00:23:11 2022

Explore the Julia sets of the Mandelbrot fractal!
Scrollwheel to zoom
RMB to move
LMB to move marker

@author: Björn Krook Willén
"""

import taichi as ti
import numpy as np
from numpy import genfromtxt

cmap = genfromtxt('cmap.csv', delimiter=',')

ti.init(arch=ti.gpu)

win_size = 700
center = [0, 0]
center_j = [0, 0]
pixels = ti.field(dtype=float, shape=(win_size*2, win_size))
scale=2
scale_j = 2
itr_lim = 2500

###############################################################################

@ti.func
def complex_sqr(z: float):
    return ti.Vector([z[0]**2 - z[1]**2, z[1] * z[0] * 2])

@ti.kernel
def paint(s: float, c1: float, c2: float, s2: float, c3: float, c4: float, p1: float, p2: float):
    for i, j in pixels:
        
        if i<int(win_size):
            x_min = c1 - s
            x_max = c1 + s
            y_min = c2 - s
            y_max = c2 + s
            x = x_min + (x_max-x_min)*(i/win_size)
            y = y_min + (y_max-y_min)*(j/win_size)
        
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
            y_min = c4 - s2
            y_max = c4 + s2
            x = x_min + (x_max-x_min)*((i-win_size)/win_size)
            y = y_min + (y_max-y_min)*(j/win_size) 
        
            z = ti.Vector([x, y], dt=float)
            c = ti.Vector([p1, p2], dt=float)
        
            itr = 0
            while z.norm() < 8 and itr < itr_lim:
                z = complex_sqr(z) + c
                itr += 1
            
            pixels[i, j] = 1 - ti.sqrt(ti.sqrt(itr/itr_lim))
            
def scr2z(i, j, scale, center):
    x_min = center[0] - scale
    x_max = center[0] + scale
    y_min = center[1] - scale
    y_max = center[1] + scale
    x = x_min + (x_max-x_min)*(2*i)
    y = y_min + (y_max-y_min)*j
    return x, y

###############################################################################

if __name__=="__main__":
    pos = np.array([[0.25,0.5]])
    idx = np.random.randint(1, 2, size=(1,))
    gui = ti.GUI("Mandelbrot fractal and corresponding julia fractals", res=(win_size*2, win_size))
    while gui.running:
        mouse_x, mouse_y = gui.get_cursor_pos()
        p1, p2 = scr2z(pos[0,0], pos[0,1], scale, center)
        paint(scale, center[0], center[1], scale_j, center_j[0], center_j[1], p1, p2)
        gui.set_image(pixels)
        if pos[0,0] < 0.5:
            gui.circles(pos, radius=5, palette=[0x068587, 0xED553B, 0xEEEEF0], palette_indices=idx)
        gui.show()
        
        if gui.get_event():
            if mouse_x < 0.5:
                if gui.event.key == "LMB":
                    if gui.event.type == ti.GUI.PRESS:
                        pos[0,0] = mouse_x
                        pos[0,1] = mouse_y 
                if gui.event.key == "Wheel":
                    if gui.event.delta[1] < 0:
                        scale = scale*1.1
                        pos[0,0] = 0.25+(pos[0,0]-0.25)/1.1
                        pos[0,1] = 0.5+(pos[0,1]-0.5)/1.1
                    else:
                        scale = scale/1.1
                        pos[0,0] = 0.25+(pos[0,0]-0.25)*1.1
                        pos[0,1] = 0.5+(pos[0,1]-0.5)*1.1
                if gui.event.key == "RMB":
                    if gui.event.type == ti.GUI.PRESS:
                        a, b = scr2z(mouse_x, mouse_y, scale, center)
                        center[0]=a
                        center[1]=b
                        pos[0,0] = pos[0,0]-mouse_x+0.25
                        pos[0,1] = pos[0,1]-mouse_y+0.5
            else:
                if gui.event.key == "Wheel":
                    if gui.event.delta[1] < 0:
                        scale_j = scale_j*1.1
                    else:
                        scale_j = scale_j/1.1
                if gui.event.key == "RMB":
                    if gui.event.type == ti.GUI.PRESS:
                        a, b = scr2z(mouse_x-0.5, mouse_y, scale_j, center_j)
                        center_j[0]=a
                        center_j[1]=b