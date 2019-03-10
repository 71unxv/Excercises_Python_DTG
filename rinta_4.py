# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 15:13:58 2019

@author: RINTA
"""

def PrintPrime(x):
    for num in x:
        sisa=0
        j=[]
        for j in range (1,num+1):
            if num%j==0:
                sisa+=1
        if sisa==2:
            print(num)
        
angka=[]
for m in range(1,100):
    angka.append(m)

prima=PrintPrime(angka)