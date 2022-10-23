# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 02:12:22 2022

@author: Björn
"""

import numpy as np
import matplotlib.pyplot as plt

canvas = np.zeros([256,256])

###############################################################################

class Rule:
    def __init__(self, c=2, n=1, nr='rand'):
        self.c = c
        self.n = n
        self.new_rule()
        self.paint()
        self.b = "".join([str(self.rule[i]) for i in range(len(self.rule))])
        
    def __repr__(self):
        return 'poop'
        
    def __str__(self):
        
        return 'cum'
    
    def new_rule(self):
        self.rule = np.random.randint(0, self.c, self.c**(2*self.n+1))
    
    def paint(self, size=[256, 256], title=True):
        self.canvas = np.zeros([size[0], size[1]])
        for i in range(len(self.canvas[0])):
            self.canvas[0,i] = np.random.randint(0, self.c)
        
        for i in range(len(self.canvas[0])-1):
            for j in range(self.n ,len(self.canvas[0])-self.n):
                query = "".join([str(self.canvas[i,j-q])[0] for q in range(-self.n, self.n+1)])
                self.canvas[i+1,j] = self.rule[int(query,self.c)]
                
        
###############################################################################

r = Rule(4,1)    

plt.figure(dpi=600)
fig = plt.imshow(r.canvas, cmap='rainbow')
fig.axes.get_xaxis().set_visible(False)
fig.axes.get_yaxis().set_visible(False)
#plt.title("Rule c" + str(r.c) + "n" + str(r.n) + "nr" + str(int(r.b, r.c)))