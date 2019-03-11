# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 10:51:30 2019

@author: RINTA
"""

import numpy as np
import matplotlib.pyplot as plt

baris = 9
kolom = 9
s = (baris,kolom)
S = np.zeros(s)

i = np.arange(0,baris,2)
j = np.arange(1,kolom,2)
i,ii = np.meshgrid(i,i)
j,jj = np.meshgrid(j,j)
i=i.ravel()
ii=ii.ravel() #klo di matlab sama seperti reshape(ii,[1,numel(ii)])
j = j.ravel()
jj=j.ravel()

S[i,ii]=1 # hasilnya sama saja dengan S[ii,jj]
S[j,jj]=1
print(S)