# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 22:53:25 2022

Sandpile simulation inspired by numberphile video

@author: Björn
"""


import numpy as np
import matplotlib.pyplot as plt
import time

img=np.zeros([100,100])
img[50,50]=200

def Alg1(img):
    
    itr=0
    
    while np.max(img)>3:
    
        indx=np.where(img>3)
        add=np.zeros([img.shape[0],img.shape[1]])
    
        for i in range(np.size(indx[0])):
        
            x=indx[0][i]
            y=indx[1][i]
            
            add[x,y]=add[x,y]-4
            add[x+1,y]=add[x+1,y]+1
            add[x-1,y]=add[x-1,y]+1
            add[x,y+1]=add[x,y+1]+1
            add[x,y-1]=add[x,y-1]+1
            
        img=img+add
        itr=itr+1
        print(itr)
    
    return img

def Alg2(img):
    
    itr=0
    
    while np.max(img)>3:
    
        indx=np.where(img>3)
        add=np.zeros([img.shape[0],img.shape[1]])
    
        for i in range(np.size(indx[0])):
        
            x=indx[0][i]
            y=indx[1][i]
            
            add[x,y]=add[x,y]-1
            print('ollon')
            if np.mod(itr,4)==0:
                add[x+1,y]=add[x+1,y]+1
                print('a')
            if np.mod(itr,4)==1:
                add[x-1,y]=add[x-1,y]+1
                print('b')
            if np.mod(itr,4)==2:
                add[x,y+1]=add[x,y+1]+1
                print('c')
            if np.mod(itr,4)==3:
                add[x,y-1]=add[x,y-1]+1
                print('d')
            
        img=img+add
        itr=itr+1
        print(itr)
        #time.sleep(0.1)
    
    return img


img=Alg1(img)

plt.figure(dpi=150)
plt.imshow(img, interpolation=None)