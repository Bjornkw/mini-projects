# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 21:42:18 2022

@author: Björn
"""

import pygame
import numpy as np
import time



class Viewer:
    def __init__(self, update_func, display_size):
        self.update_func = update_func
        pygame.init()
        self.display = pygame.display.set_mode(display_size)
    
    def set_title(self, title):
        pygame.display.set_caption(title)
    
    def start(self):
        running = True
        Z = np.random.randint(0,2,(600,600))
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            Z = self.update_func(Z)
            surf = pygame.surfarray.make_surface(Z*255.0)
            self.display.blit(surf, (0, 0))

            pygame.display.update()

        pygame.quit()

def update(image):
    rule = [0, 1, 1, 1, 1, 1, 1, 0]
    image[:,0:599] = image[:,1:600]
    
    for i in range(1,598):
        q = "".join([str(image[i-1, 598]), str(image[i, 598]), str(image[i+1, 598])])
        image[i,599] = rule[int(q, 2)]
    
    #time.sleep(0.02)
    return image.astype('uint8')

viewer = Viewer(update, (600, 600))
viewer.start()