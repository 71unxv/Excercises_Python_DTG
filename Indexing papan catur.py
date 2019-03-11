# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 09:27:53 2019

@author: HP
"""

import numpy as np

A = np.zeros((10,10))

for i in range (A.shape[0]) :
    for j in range (A.shape[1]) :
#        A [i][j] = 1
        
        if i % 2 == 1:
            A[i][j] = 1
        if j % 2 == 0:
            A[i][j] = 0
    
print (A)
        
        
       

        
        
        
        
    
    



    

 