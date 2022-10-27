# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 01:57:56 2022

Procedural cave-exploring game based on cellular automatas
super slow lol

@author: Björn
"""

if __name__ == "__main__":
    
    # Imports
    import numpy as np
    import pygame as pg
    import levelgenerator
    
    # Settings 
    display_size = [64, 64]
    scale = 15
    
    # Generate the level first
    print("Generating level")
    level = levelgenerator.Level(display_size)
    level.generate_level(10)
    level_map = level.level
    level_map = np.repeat(np.repeat(level_map, scale, axis=0), scale, axis=1)
    surf = pg.surfarray.make_surface(level_map)
    
    # Main loop
    print("Starting")
    running = True
    pg.init()
    display = pg.display.set_mode([display_size[0]*scale, display_size[1]*scale])
    while running:
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        
        display.blit(surf, (0, 0))
        pg.display.update()
        
    pg.quit()