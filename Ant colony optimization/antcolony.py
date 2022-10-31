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

def AntWalk(points, ph_level, ds_level):
    not_visited = list(range(len(points[0])))
    path = []
    path.append(np.random.permutation(not_visited)[0])
    not_visited[path[0]] = []
    while len(not_visited) > 0:
        ph = ph_level[not_visited, path[-1]]
        ds = ds_level[not_visited, path[-1]]
        prob = [i for i in range(len(not_visited))]
        
        
    return path
    
def PhUpdate(ph_level, paths):
    pass

def AntOptim(points, max_iter, alpha, beta, decay):
    
    best_path = np.zeros(len(points[0])+1)
    path_lengths = []
    ph_level = np.ones([len(points[0]), len(points[0])])
    ds_level = np.ones([len(points[0]), len(points[0])])
    
    for i in range(len(points[0])):
        for j in range(len(points[0])):
            if i == j:
                ds_level[i, j] = 0
            else:
                ds_level[i, j] = 1/LenPath(points, [i, j])
    
    for i in range(max_iter):
        paths = []
        for j in range(n_ants):
            path = AntWalk(points, ph_level, ds_level)
            paths.append(path)
            
        ph_level = PhUpdate(ph_level, paths)
    
    return ds_level, path_lengths


n_points = 25
n_ants = 25
points = np.random.random([2, n_points])
max_iter = 100
alpha = 1
beta = 2
decay = 0.02

best, lens = AntOptim(points, max_iter, alpha, beta, decay)
fig = plt.scatter(points[0], points[1])
fig.axes.get_xaxis().set_visible(False)
fig.axes.get_yaxis().set_visible(False)