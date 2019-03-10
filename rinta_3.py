# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 14:28:45 2019

@author: RINTA
"""

A = []
for i in range(1,20):
    A.append(i)         #Append = menyatukan

for x in A:
    if A[x-1] % 2 == 0:
        print('Genap')
    else:
        print('Ganjil')