# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 08:47:45 2019

@author: HP
"""
import numpy as np
import matplotlib.pyplot as plt

A = 10
t = np.linspace(0,10,11)
f = 10

Y = A * np.exp(t*-1) * np.sin(2*3.14*f*t) 
print(Y)

plt.plot(t,Y)