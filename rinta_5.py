# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 15:57:17 2019

@author: RINTA
"""

def fun_pangkat(x):
    hasil = x**x
    return hasil

num=[]
for i in range(1,10):
    hasil=fun_pangkat(i)
    print(hasil)