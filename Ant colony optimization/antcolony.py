# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 01:08:08 2022

@author: Björn
"""

import numpy as np

def LenPath(points, path):
    dist = 0
    for i in range(len((path))-1):
        dx = points[0, path[i+1]] - points[0, path[i]]
        dy = points[1, path[i+1]] - points[1, path[i]]
        dist = dist + np.linalg.norm([dx, dy])
    return dist
        
def choose_from(array):
    norm_array = array/sum(array)
    r = np.random.random()
    s = 0
    for i in range(len(array)):
        s = s + norm_array[i]
        if s>r:
            return i
    raise Exception('cum')

def AntWalk(points, ph_level, ds_level, alpha, beta):
    not_visited = np.array(range(len(points[0])), dtype=int)
    path = []
    path.append(np.random.permutation(not_visited)[0])
    np.delete(not_visited, path[0])
    while len(not_visited) > 0:
        ph = ph_level[not_visited, path[-1]]
        ds = ds_level[not_visited, path[-1]]
        p = (ph**alpha)*(ds**beta)
        idx = choose_from(p)
        choise = not_visited[idx]
        path.append(choise)
        not_visited = np.delete(not_visited, idx)
    path.append(path[0])
    return np.array(path)

    
def PhUpdate(points, ph_level, paths, decay, ph_min, Q):
    dph = ph_level*0
    for path in paths:
        l = LenPath(points, path)
        for i in range(len(path)-1):
            dph[path[i], path[i+1]] = Q/l
            dph[path[i+1], path[i]] = Q/l
    ph_level = (ph_level+dph)*(1-decay)
    for i in range(len(ph_level[0])):
        for j in range(len(ph_level[0])):
            if ph_level[i,j]<ph_min:
                ph_level[i, j] = ph_min
    return ph_level 

def AntOptim(points, max_iter=100, alpha=1, beta=2, decay=0.01, ph_min=0.01, Q=1):
    best_path = np.array(range(len(points[0])))
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
        print("iteration " + str(i) + "/" + str(max_iter))
        paths = []
        for j in range(n_ants):
            path = AntWalk(points, ph_level, ds_level, alpha, beta)
            paths.append(path)
            if LenPath(points, path) < LenPath(points, best_path):
                best_path = path
        ph_level = PhUpdate(points, ph_level, paths, decay, ph_min, Q)
        path_lengths.append(LenPath(points, best_path))
    return best_path, path_lengths, ph_level

def PlotStuff(points, best_path, lens, ph_level):
    plt.figure()
    fig = plt.scatter(points[0], points[1])
    for i in range(len(best_path)-1):
        pass
        plt.plot((points[0][best_path[i]], points[0][best_path[i+1]]), (points[1][best_path[i]], points[1][best_path[i+1]]), 'r')
    fig.axes.get_xaxis().set_visible(False)
    fig.axes.get_yaxis().set_visible(False)
    plt.figure()
    fig2 = plt.plot(range(len(lens)), lens)
    

if __name__=="__main__":
    import matplotlib.pyplot as plt
    n_points = 50
    n_ants = 100
    points = np.random.random([2, n_points])
    max_iter = 2000
    alpha = 1.5
    beta = 2.5
    decay = 0.02
    ph_min = 0.05
    Q = 1

    best, lens, ph = AntOptim(points, max_iter, alpha, beta, decay, ph_min, Q)
    PlotStuff(points, best, lens, ph)