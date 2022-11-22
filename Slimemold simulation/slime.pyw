# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 01:38:48 2022

@author: Björn
"""

import taichi as ti
import numpy as np
from PIL import Image

ti.init(arch=ti.gpu)

win_size = [400, 400]
center = [int(win_size[0]/2), int(win_size[0]/2)]
pixels = ti.field(dtype=float, shape=(win_size[0], win_size[1]))

###############################################################################

@ti.func
def complex_sqr(z: float):
    return ti.Vector([z[0]**2 - z[1]**2, z[1] * z[0] * 2])


@ti.kernel
def evaporate_trail(e: float):
    for i, j in pixels:
        pixels[i, j] = pixels[i, j]*(1-e)
        
@ti.kernel
def diffuse_trail():
    for i, j in pixels:
        s = pixels[i, j-1]+pixels[i, j+1]+pixels[i-1, j]+pixels[i+1, j]+pixels[i+1, j+1]+pixels[i+1, j-1]+pixels[i-1, j+1]+pixels[i-1, j-1]
        pixels[i, j] = s/8
        

gui = ti.GUI("Mandelbrot fractal", res=(win_size[0], win_size[1]))

###############################################################################

class Agent():
    def __init__(self):
        self.x = center[0]+np.random.random()*5
        self.y = center[1]+np.random.random()*5
        self.phi = np.random.random()*10
        
    def update(self):
        v=3
        if self.y < 10:
            self.phi=1.57
        if self.y > win_size[1]-10:
            self.phi=4.71
        if self.x < 10:
            self.phi=0
        if self.x > win_size[0]-10:
            self.phi=3.14
        self.x = self.x +np.cos(self.phi)*v
        self.y = self.y +np.sin(self.phi)*v
        pixels[int(self.x), int(self.y)] = pixels[int(self.x), int(self.y)] + 1
        
        s1 = pixels[int(self.x+3*np.cos(self.phi-0.3)), int(self.y+3*np.sin(self.phi-0.3))]
        s2 = pixels[int(self.x+3*np.cos(self.phi+0.3)), int(self.y+3*np.sin(self.phi+0.3))]
        self.phi = self.phi-0.35*np.sign(s1-s2)
        
        
class AgentContainer():
    def __init__(self, n):
        self.agents = [Agent() for i in range(n)]
        
    def update(self):
        for agent in self.agents:
            agent.update()

###############################################################################

agents = AgentContainer(100)
if __name__=="__main__":
    evap = gui.slider('Evaporation Rate', 0, 0.3, step=1)
    evap.value=0.01
    while gui.running:
        agents.update()
        evaporate_trail(evap.value)
        diffuse_trail()
        gui.set_image(pixels)
        gui.show()

            