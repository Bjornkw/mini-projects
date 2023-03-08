# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 18:47:46 2023

@author: bjorn
"""

import pygame
import numpy as np
import time

class Particle:
    def __init__(self, sim_size):
        self.sim_size = sim_size
        self.position = (np.random.random()*sim_size[0], np.random.random()*sim_size[1])
        self.velocity = np.zeros((2))
        self.mass = 5
        self.radius = 5

    def update(self, neighbours):
        acc = np.zeros((2))
        for n in neighbours:
            dx = self.position[0] - n.position[0]
            dy = self.position[1] - n.position[1]
            d_squre = dx**2 + dy**2 + 0.0001
            acc += (0.01*n.mass*np.array([-dx,-dy]))/d_squre
        self.velocity += acc
        new_pos = self.position + self.velocity
        if (new_pos[0] > 0) and (new_pos[0] < self.sim_size[0]) and (new_pos[1] > 0) and (new_pos[1] < self.sim_size[1]):
            self.position = new_pos
        else:
            self.velocity = np.zeros((2))

class Grid:
    def __init__(self, display_size, grid_size):
        self.display_size = display_size
        self.grid_size = grid_size
        self.clear()
        
    def clear(self):
        self.grid = [[[] for i in range(self.grid_size[1])] for j in range(self.grid_size[0])]
        
    def insert(self, obj, pos):
        x = int((pos[0]/self.display_size[0])*(self.grid_size[0]-1))
        y = int((pos[1]/self.display_size[1])*(self.grid_size[1]-1))
        self.grid[x][y].append(obj)
        
    def query(self, pos):
        x = int((pos[0]/self.display_size[0])*(self.grid_size[0]-1))
        y = int((pos[1]/self.display_size[1])*(self.grid_size[1]-1))
        neighbours = []
        for i in range(-2,3):
            for j in range(-2,3):
                try:
                    neighbours += self.grid[x+i][y+j]
                except:
                    pass
        return neighbours


class Simulation:
    def __init__(self, n, display_size, grid_size):
        self.display = pygame.display.set_mode(display_size)
        self.particles = [Particle(display_size) for i in range(n)]
        self.grid = Grid(display_size, grid_size)
        pygame.init()
        
    def draw(self):
        self.display.fill((0,0,0))
        for particle in self.particles:
            pygame.draw.circle(self.display, "BLUE", particle.position, particle.radius)
        
    def build_grid(self):
        self.grid.clear()
        for particle in self.particles:
            pos = particle.position
            self.grid.insert(particle, pos)
            
    def step(self):
        self.build_grid()
        for particle in self.particles:
            pos = particle.position
            neighbours = self.grid.query(pos)
            particle.update(neighbours)

    def start(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            start = time.time()
            self.step()
            self.draw()
            pygame.display.update()
            end = time.time()
            try:
                t = 1/(end-start)
            except Exception:
                t=1
            print("fps: ", t)
        pygame.quit()


if __name__=="__main__":
    N_PARTICLES = 200
    WIN_SIZE = (1200, 800)
    GRID_SIZE = (24, 16)
    sim = Simulation(N_PARTICLES, WIN_SIZE, GRID_SIZE)
    sim.start()
    