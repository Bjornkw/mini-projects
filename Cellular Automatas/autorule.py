# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 02:12:22 2022

@author: Björn
"""

import numpy as np
if __name__ == "__main__":
    import matplotlib.pyplot as plt

###############################################################################

def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(str(n % b))
        n //= b
    return ''.join(digits[::-1])

###############################################################################

class Rule:
    def __init__(self, c=2, n=1, size=[256, 256],  nr='rand'):
        self.size = size
        self.canvas = np.zeros([self.size[0], self.size[1]])
        self.c = c
        self.n = n
        self.new_rule(nr)
        self.paint_canvas()
        self.num = "".join([str(self.rule[i]) for i in range(len(self.rule))])
        
    def __str__(self):
        return "Rule object: Classes = " + str(self.c) + ", Neighbours = " +str(self.n) + "\n" + str(int(self.num, self.c))
    
    def new_rule(self, nr):
        if nr == 'rand':
            self.rule = np.random.randint(0, self.c, self.c**(2*self.n+1))
        elif type(nr) == int:
            self.rule = [0 for i in range((self.c**(self.n+2))+1-len(numberToBase(nr, self.c)))] + [int(i) for i in numberToBase(nr, self.c)]
        elif type(nr) != int:
            raise Exception('nr is not a number!')
            
    def paint_line(self, prev_line):
        line = np.zeros(len(prev_line))
        for i in range(self.n, len(prev_line)-self.n):
            query = "".join([str(prev_line[i+q])[0] for q in range(-self.n, self.n+1)])
            line[i] = self.rule[-1-int(query, self.c)]
        return line
    
    def paint_canvas(self, title=True):
        for i in range(len(self.canvas[0])):
            self.canvas[0,i] = np.random.randint(0, self.c)
        
        for i in range(len(self.canvas[0])-1):
            self.canvas[i+1,:] = self.paint_line(self.canvas[i,:])
                
###############################################################################

if __name__ == "__main__":
    r = Rule(5,1)
    print(r)
    plt.figure(dpi=400)
    fig = plt.imshow(r.canvas, cmap='rainbow')
    fig.axes.get_xaxis().set_visible(False)
    fig.axes.get_yaxis().set_visible(False)
    #plt.title("Rule " + str(int(r.num, r.c)))