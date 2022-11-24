# -*- coding: utf-8 -*-
"""
Mandelbrot renderer, real-time
Use mouse wheel to zoom in/out, and LMB to move

Created on Wed Aug 19 22:11:51 2021

@author: Björn Krook Willén
"""

import taichi as ti
import numpy as np
from PIL import Image
from numpy import genfromtxt

cmap = genfromtxt('cmap.csv', delimiter=',')

ti.init(arch=ti.gpu)

win_size = [960, 540]
win_size_s = [1920, 1080]
center = [0, 0]
pixels = ti.field(dtype=float, shape=(win_size[0], win_size[1]))
pixels_s = ti.field(dtype=ti.float64, shape=(win_size_s[0], win_size_s[1]))
scale=1
itr_lim = 2500
itr_lim_s = 5000

###############################################################################

@ti.func
def complex_sqr(z: float):
    return ti.Vector([z[0]**2 - z[1]**2, z[1] * z[0] * 2])

@ti.func
def complex_sqr_fancy(z: ti.float64):
    return ti.Vector([z[0]**2 - z[1]**2, z[1] * z[0] * 2])

@ti.kernel
def paint(s: float, c1: float, c2: float):
    for i, j in pixels:
        
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

def save_frame(d):
    print('Saving Image...')
    paint_fancy(d[0], d[1], d[2])
    image = np.zeros((win_size_s[1], win_size_s[0], 3), dtype=np.uint8)
    itr = pixels_s.to_numpy(dtype=np.float64)
    itr_mod = np.mod(itr, 64)
    for i in range(win_size_s[1]):
        for j in range(win_size_s[0]):
            if itr[j, i] == itr_lim_s:
                image[i,j,:]=0
            else:
                image[i,j,0] = cmap[int(itr_mod[j,i])][0]*255.0
                image[i,j,1] = cmap[int(itr_mod[j,i])][1]*255.0
                image[i,j,2] = cmap[int(itr_mod[j,i])][2]*255.0
    image = Image.fromarray(image, 'RGB')
    image.save("fractal.png")
    print('Done!')
    
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
    gui = ti.GUI("Mandelbrot fractal", res=(win_size[0], win_size[1]))
    mouse_x, mouse_y = 0, 0
    track = False
    while gui.running:
        mouse_x_old, mouse_y_old = mouse_x, mouse_y
        mouse_x, mouse_y = gui.get_cursor_pos()
        paint(scale, center[0], center[1])
        gui.set_image(pixels)
        gui.show()
        
        if track:
            a, b = scr2z(mouse_x, mouse_y, scale, center)
            c, d = scr2z(mouse_x_old, mouse_y_old, scale, center)
            center[0]=center[0]+(c-a)/2
            center[1]=center[1]+(d-b)/(win_size[0]/win_size[1])
    
        if gui.get_event():
            if gui.event.key == "Wheel":
                if gui.event.delta[1] > 0:
                    scale = scale/1.3
                else:
                    scale = scale*1.3
                    
            if gui.event.key == "Control_L":
                save_frame([scale, center[0], center[1]])
                
            if gui.event.key == "LMB":
                if gui.event.type == ti.GUI.PRESS:
                    track = True
                if gui.event.type == ti.GUI.RELEASE:
                    track = False
            