# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 15:01:57 2019

@author: Almarsa
"""
def PPrime(x):
    for item in x:
        jumlah = 0
        for i in range(1,item+1):
            if item % i == 0:
                jumlah += 1
           
        if jumlah == 2:
            print('adalah bilangan prima')
        else:
            print('bukan bilangan prima')

A = []
for i in range(1,11):
    A.append(i)

PPrime(A)
          