# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 19:34:50 2022

@author: Björn
"""

import numpy as np
from numpy import genfromtxt
from numba import jit, njit, prange
import pygame as pg
import time

#------------------------------------------------------------------------------

win_size = [320, 240]
level = genfromtxt('level.csv', delimiter=',')
level = level*(-1) +1
c_palett = {"white": (0,0,0), "red": (1,0,0)}

#------------------------------------------------------------------------------

class Character():
    def __init__(self):
        self.x = 32
        self.y = 38
        self.phi = 0
        
    def move(self, r):
        ds = 0.5*r
        new_x = self.x + ds*np.cos(self.phi)
        new_y = self.y + ds*np.sin(self.phi)
        if level[int(new_x), int(new_y)]==0:
            self.x = new_x
            self.y = new_y
        else:
            pass
        
#------------------------------------------------------------------------------     

@jit
def CastRay(x, y, phi, s):
    stepsize=s
    max_steps=128
    for i in prange(1, max_steps):
        px1 = x-int(x)
        py1 = y-int(y)
        px2 = px1 + np.cos(phi)
        py2 = py1 + np.sin(phi)
        b = (py1*px2-py2*px1)/(px2-px1)
        m = (py2-py1)/(px2-px1)
        x = x + np.cos(phi)*stepsize
        y = y + np.sin(phi)*stepsize
        if level[int(x), int(y)]==1:
            break
    return i, level[int(x),int(y)]

@jit
def Draw(x, y, phi, s, W, H):
    FoV = 2     # Radians
    frame = np.zeros((W, H, 3))
    
    rays = []
    for i in prange(W):
        ray_angle = phi - 0.5*FoV + ((i+1)/W)*FoV
        rays.append(CastRay(x, y, ray_angle, s))
        
    for i in prange(len(rays)):
        dist = rays[i][0]*s
        mat = rays[i][1]
        s_fac = int(H/dist)
        a = int((H-s_fac)/2)
        b = int((s_fac+H)/2)
        frame[i, a:b, :] = 1/(1+dist)
        
    return frame

#------------------------------------------------------------------------------

if __name__ == "__main__":
    char = Character()
    pg.init()
    display = pg.display.set_mode((win_size[0]*2, win_size[1]*2))
    RUNNING = True
    while RUNNING:
        start = time.time()
        keys=pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            char.phi = char.phi-0.1
        if keys[pg.K_RIGHT]:
            char.phi = char.phi+0.1
        if keys[pg.K_UP]:
            char.move(1)
        if keys[pg.K_DOWN]:
            char.move(-1)
            
        for event in pg.event.get():
            if event.type == pg.QUIT:
                RUNNING = False
        
        W = win_size[0]
        H = win_size[1]
        frame = Draw(char.x, char.y, char.phi, 0.05, W, H)*255.0
        frame = frame.repeat(2,axis=0).repeat(2,axis=1)
        surf = pg.surfarray.make_surface(frame)
        display.blit(surf, (0, 0))
        pg.display.update()
        end = time.time()
        print("fps: ", 1/(end-start))
    pg.quit()