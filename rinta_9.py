# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 09:33:08 2019

@author: RINTA
"""

import numpy as np
import matplotlib.pyplot as plt

s = (9,9)
S = np.zeros(s)

for x in range (1,9):
    if (x-1)%2==1:
        for y in range (1,9):
            if (y-1)%2==1:
                S[x-1][y-1]=1
        
print(S)