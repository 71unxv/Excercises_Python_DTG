# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 18:18:38 2019

@author: RINTA
"""

def Kalkulator(A,B,command):
    if command==1:
        hasil = A+B
        return hasil
    elif command==2:
        hasil = A-B
        return hasil
    elif command == 3:
        hasil = A*B
        return hasil
    elif command == 4:
        hasil = A/B
        return hasil
    elif command == 5:
        hasil = A%B
        return hasil

A = int(input('Masukan nilai A : '))
B = int(input('Masukan nilai B : '))
print('-------------------------------------')
print ('Opsi operasi matematika')
print('1. Penjumlahan')
print('2. Pengurangan')
print('3. Perkalian')
print('4. Pembagian')
print('5. Sisa pembagian (mod)')
print('-------------------------------------')
command=int(input('Pilihan anda adalah :'))

hasil = Kalkulator(A,B,command)
print(hasil)