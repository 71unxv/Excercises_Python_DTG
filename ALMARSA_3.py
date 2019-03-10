# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 14:26:34 2019

@author: Almarsa
"""

A = []
for i in range(1,20):
    A.append(i)

for i in A:
    if A[i-1]%2 == 0:
        print('genap')
    else:
        print('ganjil')