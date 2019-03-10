from KALKULATOR.MaulCalculator import *



print('-------------SELAMAT DATANG-------------')
print('-------------KALKULATOR MAUL------------')

A = int(input('Masukkan angka pertama :'))
B = int(input('Masukkan angka kedua :'))

print('----------------------------------------')
print('Berikut list program kalkulator yang tersedia:')
print('1. Penjumlahan')
print('2. Pengurangan')
print('3. Pengalian')
print('4. Pembagian')

print('Silahkan input metod yang anda inginkan! ')
command = int(input())

C = Perhitungan(A,B,command)
print(f'Selamat perhitungan anda berhasil, Hasilnya adalah {C}')

def Perhitungan(A,B,command):
    if command == 1:
        C = Kalkulator.Penjumlahan(A,B)
        return C
    elif command == 2:
        C = Kalkulator.Pengurangan(A,B)
        return C
    elif command == 3:
        C = Kalkulator.Pengalian(A,B)
        return C
    elif command == 4:
        C = Kalkulator.Pembagian(A,B)
        return C