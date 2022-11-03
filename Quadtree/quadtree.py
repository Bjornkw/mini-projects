# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 00:02:14 2022

@author: Björn
"""


class QuadTree():
    def __init__(self, layer=0, bounds=[0,0,1,1]):
        self.layer = layer
        self.points =[]
        self.maxpoints = 5
        self.bounds = bounds
        self.children = False
    
    def add_point(self, point):
        self.points.append(point)
        if (len(self.points) > self.maxpoints) or self.children:
            self.children = True
            midpoint = [(self.bounds[0]-self.bounds[2])/2, (self.bounds[1]-self.bounds[3])/2]
            self.q1 = QuadTree(self.layer+1, [midpoint[0], self.bounds[2], midpoint[1], self.bounds[3]])
            self.q2 = QuadTree(self.layer+1, [self.bounds[0], midpoint[0], midpoint[1], self.bounds[3]])
            self.q3 = QuadTree(self.layer+1, [self.bounds[0], midpoint[0], self.bounds[1], midpoint[1]])
            self.q4 = QuadTree(self.layer+1, [midpoint[0], self.bounds[2], self.bounds[2], midpoint[1]])
            for point in self.points:
                if point[0] > midpoint[0]:
                    if point[1] > midpoint[1]:
                        self.q1.add_point(point)
                    else:
                        self.q4.add_point(point)
                else:
                    if point[1] > midpoint[1]:
                        self.q2.add_point(point)
                    else:
                        self.q3.add_point(point)
            self.points = []
                    
        else:
            self.points.append(point)
    
if __name__ == "__main__":
    import numpy as np
    import matplotlib.pyplot as plt
    import time
    
    points = [np.random.random([2]) for i in range(20)]
    tree = QuadTree()
    for point in points:
        tree.add_point(point)