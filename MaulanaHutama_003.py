# -*- coding: utf-8 -*-

A = []
for item in range(1,20):
    A.append(item)

for i in A:
    if A[i-1] % 2 == 0:
        print('Genap')
    else:
        print('Ganjil')