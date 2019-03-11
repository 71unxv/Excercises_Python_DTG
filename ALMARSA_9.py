# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 09:25:29 2019

@author: Almarsa
"""

import numpy as np
import matplotlib.pyplot as plt

l = (10,10)
A = np.zeros(l)

for i in range(1,A.shape[0]-1):
    for j in range(1,A.shape[1]-1):
        if i % 2 == 1 and j % 2 == 1:
            A[i][j] = 1
        if i % 2 == 0 and j % 2 == 0:
            A[i][j] = 1
    
print(A)



    