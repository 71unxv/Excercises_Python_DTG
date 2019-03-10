# -*- coding: utf-8 -*-

def PrintPrime(A):
    for item in A:
        isi = 0
        for i in range(1,item+1):
            if item % i == 0:
                isi += 1
        if isi == 2:
            print(f'Angka {item} Adalah Bilangan Prima')
        else:
            print(f'Angka {item} Bukanlah Bilangan Prima')       

PrintPrime([1,2,3,4,5,6,7,8,9,10])