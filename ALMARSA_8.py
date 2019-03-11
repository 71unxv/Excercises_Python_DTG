# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 08:33:51 2019

@author: Almarsa
"""

import numpy as np
import matplotlib.pyplot as plt

A = 1
w = 2 * 3.14
f = 100
t = np.linspace(0,100,101)

y = A * np.exp(-t) * np.sin(w*t*f)
print(y)

plt.plot(t,y)