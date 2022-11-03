# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 00:02:14 2022

@author: Björn
"""

###############################################################################

class point():
    def __init__(self, x, y, idx=None):
        self.x = x
        self.y = y
        self.idx = idx
        
    def __str__(self):
        return ("Point " + str(self.idx) + ": x = " + str(self.x) + ", y = " + str(self.y))
        
###############################################################################

class QuadTree():
    def __init__(self, layer=0, bounds=[0,0,1,1]):
        self.layer = layer
        self.points =[]
        self.maxpoints = 5
        self.bounds = bounds
        self.midpoint = [(bounds[2]-bounds[0])/2, (bounds[3]-bounds[1])/2]
        self.children = False
        
    def __str__(self):
        return "Quadtree at layer " + str(self.layer)
    
    def add_single_point(self, point):
        if self.children:
            self.add_to_children(point)
        else:
            self.points.append(point)
            
    def add_points(self, points):
        for point in points:
            self.add_single_point(point)
            
    def add_to_children(self, point):
        pass
    
###############################################################################
    
if __name__ == "__main__":
    import numpy as np
    import matplotlib.pyplot as plt
    import time
    
    points = [point(np.random.random(), np.random.random(), i) for i in range(10000)]
    tree = QuadTree()
    start = time.time()
    tree.add_points(points)
    end = time.time()
    print(end-start)