# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 17:45:59 2019

@author: Almarsa
"""

class calculator:
    def tambah(x, y):
        return x + y
    def kurang(x, y):
        return x - y
    def bagi(x, y):
        return x / y
    def kali(x, y):
        return x * y


    
print("select operation")
print('1. Penjumlahan')
print('2. Pengurangan')
print('3. Perkalian')
print('4. Pembagian')

choice = (input('pilih operasi matematis'))
command = int(input())

number1 = int(input('first number :'))
number2 = int(input('second number :'))

def operasi(number1, number2, command):
    if command == 1:
        A = calculator.tambah(number1, number2)
        return A
    if command == 2:
        A = calculator.kurang(number1,number2)
        return A
    if command == 3:
        A = calculator.kali(number1,number2)
        return A
    if command == 4:
        A = calculator.bagi(number1,number2)
        return A
    
hasil = operasi(number1, number2, command)
print(f"hasil perhitungan : {hasil}")


        
    
    

     