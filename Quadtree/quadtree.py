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
        self.has_children = False
        self.q1 = None
        self.q2 = None
        self.q3 = None
        self.q4 = None
        
    def __str__(self):
        return "Quadtree at layer " + str(self.layer)
    
    def add_single_point(self, point):
        if self.has_children:
            self.add_to_children(point)
        else:
            if len(self.points) < self.maxpoints+1:
                self.points.append(point)
            else:
                self.has_children = True
                self.make_children()
                self.add_to_children(point)
                for p in self.points:
                    self.add_to_children(p)
                self.points = []
            
    def add_points(self, points):
        for point in points:
            self.add_single_point(point)
            
    def make_children(self):
        x_min = self.bounds[0]
        y_min = self.bounds[1]
        x_max = self.bounds[2]
        y_max = self.bounds[3]
        self.q1 = QuadTree(self.layer+1, [self.midpoint[0], self.midpoint[1], x_max, y_max])
        self.q2 = QuadTree(self.layer+1, [x_min, self.midpoint[1], self.midpoint[0], y_max])
        self.q3 = QuadTree(self.layer+1, [self.midpoint[0], y_min, x_max, self.midpoint[1]])
        self.q4 = QuadTree(self.layer+1, [x_min, y_min, self.midpoint[0], self.midpoint[1]])
        
            
    def add_to_children(self, point):
        if point.x >= self.midpoint[0]:
            if point.y >= self.midpoint[1]:
                self.q1.add_single_point(point)
            else:
                self.q4.add_single_point(point)
        else:
            if point.y >= self.midpoint[1]:
                self.q2.add_single_point(point)
            else:
                self.q3.add_single_point(point)
                
    def query(self, point, radius):
        pass
    
    
###############################################################################
    
if __name__ == "__main__":
    import numpy as np
    import matplotlib.pyplot as plt
    import time
    
    points = [point((np.random.random()+0.01)/1.02, np.random.random(), i) for i in range(20)]
    tree = QuadTree()
    start = time.time()
    tree.add_points(points)
    end = time.time()
    print(end-start)