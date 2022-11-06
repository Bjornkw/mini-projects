# -*- coding: utf-8 -*-
"""
Mandelbrot renderer, real-time
Use mouse buttons to zoom in/out

Created on Wed Aug 19 22:11:51 2021

@author: Björn Krook Willén
"""

import taichi as ti
import numpy as np

ti.init(arch=ti.gpu)

win_size = [1000, 700]
center = [0, 0]
pixels = ti.field(dtype=float, shape=(win_size[0], win_size[1]))
pixels_s = ti.field(dtype=ti.float64, shape=(1920, 1080))
scale=1
itr_lim = 2500

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

gui = ti.GUI("Mandelbrot fractal", res=(win_size[0], win_size[1]))

@ti.kernel
def paint_fancy(s: ti.float64, c1: ti.float64, c2: ti.float64, i_lim: int):
    for i, j in pixels_s:
        
        x_min = c1 - s
        x_max = c1 + s
        y_min = c2 - s*(win_size[1]/win_size[0])
        y_max = c2 + s*(win_size[1]/win_size[0])
        x = x_min + (x_max-x_min)*(i/win_size[0])
        y = y_min + (y_max-y_min)*(j/win_size[1])
        
        z = ti.Vector([0, 0], dt=ti.float64)
        c = ti.Vector([x, y], dt=ti.float64)
        
        itr = 0
        while z.norm() < 16 and itr < i_lim:
            z = complex_sqr(z) + c
            itr += 1
            
        pixels_s[i, j] = itr

gui = ti.GUI("Mandelbrot fractal", res=(win_size[0], win_size[1]))

###############################################################################

def save_frame(d):
    print('bajs')
    paint_fancy(d[0], d[1], d[2], 50000)
    image = pixels_s.to_numpy(dtype=np.float64)
    np.savetxt("img.csv", image, delimiter=",")
    return image


###############################################################################

i = 0
while gui.running:
    paint(scale, center[0], center[1])
    gui.set_image(pixels)
    gui.show()
    
    if gui.get_event(ti.GUI.PRESS):
        print(gui.event.key)
        print("[" + str(scale) + ", " +str(center[0])+ ", "+str(center[1])+ "]")
        mouse_x, mouse_y = gui.get_cursor_pos()
        center=[center[0] + (mouse_x -0.5)*scale, center[1] + (mouse_y -0.5)*(win_size[1]/win_size[0])*scale]
        
        if gui.event.key == "LMB":
            scale = scale/1.3
        elif gui.event.key =="RMB":
            scale = scale*1.3
        elif gui.event.key == "Control_L":
            save_frame([scale, center[0], center[1]])
            