# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 01:29:10 2022

@author: Björn
"""

import numpy as np
    
###############################################################################

class Canvas():
    def __init__(self, size):
        self.size = size
        self.fill_noise()
    
    def fill_noise(self):
        self.canvas = np.random.randint(0, 2, [self.size[0], self.size[1]])
    
    def iterate(self, n):
        for s in range(n):
            canvas_tmp = np.zeros([self.size[0], self.size[1]])
            
            for i in range(1, self.size[0]-1):
                for j in range(1, self.size[1]-1):
                    n_sum = sum(sum(np.array([[self.canvas[i+p,j+q] for p in range(-1,2)] for q in range(-1,2)])))
                    
                    if self.canvas[i, j] == 1:
                        if n_sum-1 < 4:
                            canvas_tmp[i, j] = 0
                    if canvas_tmp[i,j] == 0:
                        if n_sum > 4:
                            canvas_tmp[i, j] = 1     
                    else: 
                        canvas_tmp[i, j] = np.copy(self.canvas[i, j])

            self.canvas = np.copy(canvas_tmp)

###############################################################################

if __name__ == "__main__":
    import matplotlib.pyplot as plt
    size = [64, 64]
    c = Canvas(size)
    c.iterate(30)
    plt.figure(dpi=200)
    img = c.canvas*(-1)+1
    fig = plt.imshow(img, cmap='Greys')
    fig.axes.get_xaxis().set_visible(False)
    fig.axes.get_yaxis().set_visible(False)