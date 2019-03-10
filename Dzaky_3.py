# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 14:28:47 2019

@author: gayuh
"""

number=[]
for i in range(1,20):
    number.append(i)

for i in number:
    if number[i-1] % 2 == 0:
        print('Genap')
    else:
        print('Ganjil')