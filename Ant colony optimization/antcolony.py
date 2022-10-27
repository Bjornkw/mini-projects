# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 01:08:08 2022

@author: Björn
"""

import numpy as np
import matplotlib.pyplot as plt

def LenPath(points, path):
    dist = 0
    for i in range(len((path))-1):
        dx = points[0, path[i+1]] - points[0, path[i]]
        dy = points[1, path[i+1]] - points[1, path[i]]
        dist = dist + np.linalg.norm([dx, dy])
        
    return dist

def AntWalk(points, pheromone_level):
    pass

    #return path

def AntOptim(points, max_iter):
    
    current_path = np.zeros(len(points[0]))
    best_path = np.zeros(len(points[0]))
    path_lengths = []
    pheromone_level = np.zeros([len(points[0]), len(points[0])])
    
    for i in range(max_iter):
        pass
    
    return best_path, path_lengths


n_points = 25
n_ants = 25
points = np.random.random([2, n_points])
max_iter = 100

AntOptim(points, max_iter)
fig = plt.scatter(points[0], points[1])
fig.axes.get_xaxis().set_visible(False)
fig.axes.get_yaxis().set_visible(False)