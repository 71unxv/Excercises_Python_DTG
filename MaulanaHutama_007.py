# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

#A = 2 #Ampltiude
#f = 100
#t = np.linspace(0,100,101)
#
#y = A * np.exp(t*-1) * np.sin(2*3.14*f*t)
#print(y)
#plt.plot(t,y)

#class Catur():
#    def __ini__(self):
#        self.besar = np.zeros([10,10])
#    
#    def gantiBesar(A):
#        self.besar = np.zeros(A)
#        return self.besar
#    

catur = np.zeros([9,9])

for ii in range(1,catur.shape[0]-1):
    for jj in range(1,catur.shape[1]-1):
        if ii % 2 == 1 and jj % 2 == 1:
            catur[ii][jj] = 1
#        elif ii % 2 == 0 and jj % 2 == 0:
#            catur[ii][jj] = 1
            
print(catur)
plt.pcolor(catur)