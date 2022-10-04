# -*- coding: utf-8 -*-
"""
Mandelbrot renderer, real-time
Use mouse buttons to zoom in/out

Created on Wed Aug 19 22:11:51 2021

@author: Björn Krook Willén
"""

import taichi as ti

ti.init(arch=ti.gpu)

win_size = [1000, 700]
center = [-1.575, 0]
pixels = ti.field(dtype=float, shape=(win_size[0], win_size[1]))
scale=0.002
itr_lim = 2500

@ti.func
def complex_sqr(z: float):
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

i = 0
while gui.running:
    paint(scale, center[0], center[1])
    gui.set_image(pixels)
    gui.show()
    
    if gui.get_event(ti.GUI.PRESS):
        mouse_x, mouse_y = gui.get_cursor_pos()
        center=[center[0] + (mouse_x -0.5)*scale, center[1] + (mouse_y -0.5)*(win_size[1]/win_size[0])*scale]
        
        if gui.event.key == "LMB":
            scale = scale/1.3
        else:
            scale = scale*1.3