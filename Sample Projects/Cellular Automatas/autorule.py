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
    def __init__(self, c=2, n=1, size=[256, 256],  nr='rand'):
        self.size = size
        self.c = c
        self.n = n
        self.new_rule(nr)
        self.paint()
        self.num = "".join([str(self.rule[i]) for i in range(len(self.rule))]), self.c
        
    def __repr__(self):
        return 'poop'
        
    def __str__(self):
        
        return 'cum'
    
    def new_rule(self, nr):
        if nr == 'rand':
            self.rule = np.random.randint(0, self.c, self.c**(2*self.n+1))
        elif type(nr) == int:
            self.rule = [0 for i in range(11-len(bin(nr)))] + [int(i) for i in bin(nr)[2:]]
        elif type(nr) != int:
            raise Exception('nr is not a number!')
            
    
    def paint(self, title=True):
        self.canvas = np.zeros([self.size[0], self.size[1]])
        #for i in range(len(self.canvas[0])):
            #self.canvas[0,i] = np.random.randint(0, self.c)
        self.canvas[0,128] = 1
        
        for i in range(len(self.canvas[0])-1):
            for j in range(self.n ,len(self.canvas[0])-self.n):
                query = "".join([str(self.canvas[i,j+q])[0] for q in range(-self.n, self.n+1)])
                self.canvas[i+1,j] = self.rule[-1-int(query,self.c)]
                
        
###############################################################################

r = Rule(2,1,nr=30)    

plt.figure(dpi=600)
fig = plt.imshow(r.canvas, cmap='rainbow')
fig.axes.get_xaxis().set_visible(False)
fig.axes.get_yaxis().set_visible(False)
plt.title("Rule " + str(int(r.num, r.c)))