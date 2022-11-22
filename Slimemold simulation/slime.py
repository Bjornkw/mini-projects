# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 01:38:48 2022

@author: Björn
"""

import taichi as ti
import numpy as np
from PIL import Image

ti.init(arch=ti.gpu)

win_size = [500, 500]
center = [int(win_size[0]/2), int(win_size[0]/2)]
pixels = ti.field(dtype=float, shape=(win_size[0], win_size[1]))

###############################################################################

@ti.func
def complex_sqr(z: float):
    return ti.Vector([z[0]**2 - z[1]**2, z[1] * z[0] * 2])


@ti.kernel
def evaporate_trail():
    for i, j in pixels:
        pixels[i, j] = pixels[i, j]*0.97
        
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
        
class AgentContainer():
    def __init__(self, n):
        self.agents = [Agent() for i in range(n)]
        
    def update(self):
        v = 3
        for agent in self.agents:
            if agent.y < 10:
                agent.phi=1.57
            if agent.y > win_size[1]-10:
                agent.phi=4.71
            if agent.x < 10:
                agent.phi=0
            if agent.x > win_size[0]-10:
                agent.phi=3.14
            agent.x = agent.x +np.cos(agent.phi)*v
            agent.y = agent.y +np.sin(agent.phi)*v
            pixels[int(agent.x), int(agent.y)]=5
            
            s1 = pixels[int(agent.x+3*np.cos(agent.phi-0.3)), int(agent.y+3*np.sin(agent.phi-0.3))]
            s2 = pixels[int(agent.x+3*np.cos(agent.phi+0.3)), int(agent.y+3*np.sin(agent.phi+0.3))]
            agent.phi = agent.phi-0.25*np.sign(s1-s2)
            

###############################################################################

agents = AgentContainer(150)
if __name__=="__main__":
    while gui.running:
        agents.update()
        evaporate_trail()
        diffuse_trail()
        gui.set_image(pixels)
        gui.show()

            