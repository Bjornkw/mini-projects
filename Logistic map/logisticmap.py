# -*- coding: utf-8 -*-
"""
Slightly shitty (ineffective) logistic map calculator

Created on Mon Nov 22 23:39:30 2021

@author: Björn Krook willén
"""

import matplotlib.pyplot as plt
import numpy as np


##---------------------------PARAMETERS-------------------------------------##

maxiter=200
maxpoints=1850
xres=1000


##-----------------------ITERATION FUNCTION---------------------------------##

def Itr(lam,n):
    return lam*n*(1-n)


##-----------------COMPUTE FIXED POINTS FUNCTION----------------------------##

def Comp(lam,maxiter):
    
    n=0.5
    output=list(np.ones(maxpoints))
    
    for i in range(maxiter):
        n=Itr(lam,n)
        
    for i in range(maxpoints):
        n=Itr(lam,n)
        output[i]=n

    return output


##-----------------------------MAIN-----------------------------------------##

lam=np.linspace(3.5,4,xres)
plt.figure(dpi=400)

for i in range(xres):
    y=Comp(lam[i],maxiter)
    x=list(lam[i]*np.ones(len(y)))
    plt.scatter(x,y,0.01,np.array([0.188, 0.416, 0.592, 0.02]))

title='preiterations = '+str(maxiter)+', points = '+str(maxpoints)+', resolution = '+ str(xres)
plt.suptitle(title)