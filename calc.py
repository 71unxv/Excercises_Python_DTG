# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 17:20:54 2019

@author: gayuh
"""

# fungsi operasi
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y
def remain(x, y):
    return x % y

print("KALKULATOR ALAKADARNYA")
# menu operasi
print("Pilih Operasi.")
print("1.Jumlah")
print("2.Kurang")
print("3.Kali")
print("4.Bagi")
print("5.Sisa Pembagian")

# Meminta input dari user
choice = input("Masukkan pilihan(1/2/3/4/5): ")
num1 = int(input("Masukkan bilangan pertama: "))
num2 = int(input("Masukkan bilangan kedua: "))
if choice == '1':
    print(num1,"+",num2,"=", add(num1,num2))
elif choice == '2':
    print(num1,"-",num2,"=", subtract(num1,num2))
elif choice == '3':
    print(num1,"*",num2,"=", multiply(num1,num2))
elif choice == '4':
    print(num1,"/",num2,"=", divide(num1,num2))
elif choice == '5':
    print(num1,"/",num2,"=", remain(num1,num2))
else:
   print("Input salah")