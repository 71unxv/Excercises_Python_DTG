# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 14:23:00 2019

@author: ASUS
"""

A = []
for i in range (1, 22):
    A.append(i)

for x in A:
    if A[x-1] % 2 == 0: #jika modulu ax-1 terhadap 2 sama dengan 0, dia genap 
        print('Genap')
    else :
        print('Ganjil')
    