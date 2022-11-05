# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 01:17:27 2022

@author: Björn
"""

import numpy as np

class boid():
    def __init__(self, x, y, phi):
        self.x = x
        self.y = y
        self.phi = phi
        self.v = 1
        
    def move(self, dt):
        self.x = np.cos(self.phi)*self.v*dt
        self.y = np.sin(self.phi)*self.v*dt
        

if __name__=="__main__":
    import pygame as pg
    
    boids = [boid(np.random.random(), np.random.random(), np.random.random()*6.28) for i in range(20)]
    
    def update():
        for i in boids:
            phi_avg = 0
            for j in boids:
                if i == j:
                    pass
                
    
    def draw():
        pass
    
    RUNNING = True
    while RUNNING:
        update()
        draw()
    
    