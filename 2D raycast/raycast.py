# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 19:34:50 2022

@author: Björn
"""

import numpy as np
from numpy import genfromtxt
import pygame as pg

#------------------------------------------------------------------------------

win_size = [320, 240]

#------------------------------------------------------------------------------

level = genfromtxt('level.csv', delimiter=',')
level = level*(-1) +1


class Character():
    def __init__(self):
        self.x = 32
        self.y = 38
        self.phi = 0
        
    def move(self, r):
        ds = 0.2*r
        new_x = self.x + ds*np.cos(self.phi)
        new_y = self.y + ds*np.sin(self.phi)
        if level[int(new_x), int(new_y)]==0:
            self.x = new_x
            self.y = new_y
        else:
            pass
        
#------------------------------------------------------------------------------

def CastRay(x, y, phi):
    stepsize=0.4
    max_steps=128
    for i in range(max_steps):
        x = x + np.cos(phi)*stepsize
        y = y + np.sin(phi)*stepsize
        if level[int(x), int(y)]==1:
            break
    return i, level[int(x),int(y)]

def Draw(x, y, phi):
    frame = np.zeros([win_size[0], win_size[1], 3])
    FoV = 1     # Radians
    
    rays = []
    for i in range(win_size[0]):
        ray_angle = phi - 0.5*FoV + ((i+1)/win_size[0])*FoV
        rays.append(CastRay(x, y, ray_angle))
        
    for i in range(len(rays)):
        dist = rays[i][0]
        a = int(dist)
        frame[i, a:(win_size[1]-a),0] = 10/(dist+0.01)
    return frame

#------------------------------------------------------------------------------

if __name__ == "__main__":
    char = Character()
    pg.init()
    display = pg.display.set_mode((win_size[0]*2, win_size[1]*2))
    RUNNING = True
    while RUNNING:
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
        
        frame = Draw(char.x, char.y, char.phi)*255.0
        frame = frame.repeat(2,axis=0).repeat(2,axis=1)
        surf = pg.surfarray.make_surface(frame)
        display.blit(surf, (0, 0))
        pg.display.update()
    pg.quit()