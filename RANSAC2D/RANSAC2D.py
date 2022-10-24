# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 13:23:27 2022

A 2D RANSAC test algorithm
Linefitting while ignoring outlier points

@author: Björn Krook Willén
"""

import numpy as np
import matplotlib.pyplot as plt

def inliers(points, k, m, thresh):
    
    n=np.size(points,0)
    residuals=np.zeros(n)
    
    for i in range(n):
        residuals[i]=np.sqrt(((m+k*points[i,0]-points[i,1])**2)/(k**2+1))
    
    return np.size(np.where(residuals<thresh))

def RANSAC2D(points, thresh):
    
    n=np.size(points,0)
    inl_best=0
    
    for i in range(2000):
        
        p1=np.random.randint(n)
        p2=np.random.randint(n)
        dx=points[p1,0]-points[p2,0]
        dy=points[p1,1]-points[p2,1]
        k=dy/dx
        m=points[p1,1]-k*points[p1,0]
        inl=inliers(points, k, m, thresh)
        
        if inl>inl_best:
            inl_best=inl
            k_best=k
            m_best=m
        
        
    return [k_best, m_best]

def generateData(inliers, outliers):
    
    k=20*np.random.random()-10
    m=4*np.random.random()-2
    
    oul=6*np.random.random([outliers,2])-3
    x=np.random.random(inliers)
    y=k*x+m
    inl=np.transpose([x,y])
    pts=np.concatenate((inl, oul))
    
    return pts


pts=generateData(20,180)

A=RANSAC2D(pts, 0.02)
X=[0,1]
Y=[A[1], A[0]+A[1]]
plt.scatter(pts[:,0],pts[:,1])
plt.plot(X,Y,'r')