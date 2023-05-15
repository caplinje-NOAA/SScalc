# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 12:41:21 2023

@author: james.caplinger
"""

import numpy as np
import matplotlib.pyplot as plt
TL = 15
SL1 = 190
SL2 = 189
SL3 = 176
separation = 100

# make grid
nx=100
ny=100
x = np.linspace(0,1e3,num=nx)
y = np.linspace(0,1e3,num=ny)
center = [(np.max(x)-np.min(x))/2,(np.max(y)-np.min(y))/2]
pos1 = [0.0+center[0],np.sqrt(3/16)*separation+center[1]]
pos2 = [-0.5*separation+center[0],-np.sqrt(3/16)*separation+center[1]]
pos3 = [0.5*separation+center[0],-np.sqrt(3/16)*separation+center[1]]



def dist(point1:[float],point2:[float])->float:
    return np.sqrt(np.abs(point1[0]-point2[0])**2+np.abs(point1[1]-point2[1])**2)

print(dist(pos1,pos2),dist(pos2,pos3),dist(pos1,pos3))

L = np.zeros((nx,ny))
[Lss1,Lss2,Lss3] = [np.zeros((nx,ny)),np.zeros((nx,ny)),np.zeros((nx,ny))]
for i,xval in enumerate(x):
    for j,yval in enumerate(y):
        [dist1,dist2,dist3] = [dist([xval,yval],pos1),dist([xval,yval],pos2),dist([xval,yval],pos3)]
        [L1,L2,L3] = [SL1-TL*np.log10(dist1),SL2-TL*np.log10(dist2),SL3-TL*np.log10(dist3)]
        L[i,j] = 10*np.log10( 10**(L1/10)+10**(L2/10)+10**(L3/10) )
        
fig,ax = plt.subplots(1,1)

ax.contourf(x,y,L)
CS = ax.contour(x, x, L, [160])
ax.clabel(CS, inline=True, fontsize=10)


    
    