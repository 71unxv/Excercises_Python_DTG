# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 14:28:44 2019

@author: HP
"""
X = [         ]
for bilangan in range(1,21):
    X.append(bilangan)

for angka in X:
    if X[angka-1] % 2 == 0:
        print('Genap')
    else:
        print('Ganjil')