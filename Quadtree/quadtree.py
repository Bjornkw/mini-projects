# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 00:02:14 2022

@author: Björn Krook Willén
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
    def __init__(self, depth=0, bounds=[0,0,1,1]):
        self.layer = depth
        self.maxdepth = 5
        self.bounds = bounds
        self.midpoint = [(bounds[2]-bounds[0])/2, (bounds[3]-bounds[1])/2]
        self.children = []
        self.points = []
        self.maxpoints = 10
        self.q1 = None
        self.q2 = None
        self.q3 = None
        self.q4 = None

        
    def insert(self, points):
        pass
    
    def subdivide(self):
        
        boundsq1 = 0
        boundsq2 = 0
        boundsq3 = 0
        boundsq4 = 0
        
        self.q1 = QuadTree(self.depth+1, boundsq1)
        self.q2 = QuadTree(self.depth+1, boundsq2)
        self.q3 = QuadTree(self.depth+1, boundsq3)
        self.q4 = QuadTree(self.depth+1, boundsq4)
        
    def is_inside(self, point):
        if (self.bounds[0] < point.x < self.bounds[2]) and (self.bounds[1] < point.y < self.bounds[3]):
            return True
        else:
            return False
    
    def query(self, vec, r):
        pass
        

    
###############################################################################
    
if __name__ == "__main__":
    import numpy as np
    import matplotlib.pyplot as plt
    import time
    
    points = [point((np.random.random()+0.01)/1.02, np.random.random(), i) for i in range(20)]
    tree = QuadTree()
    start = time.time()
    tree.insert(points)
    end = time.time()
    print(end-start)