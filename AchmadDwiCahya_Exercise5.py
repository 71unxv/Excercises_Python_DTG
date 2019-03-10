def penjumlahan(x, y):
   return x + y

def pengurangan(x, y):
   return x - y

def perkalian(x, y):
   return x * y

def pembagian(x, y):
   return x / y

print("Monggo Dipilih.")
print("1.penjumlahan")
print("2.pengurangan")
print("3.perkalian")
print("4.pembagian")

pilihan = input("Masukkan pilihan(1/2/3/4): ")
angka_pertama = int(input("Masukkan bilangan pertama: "))
angka_kedua = int(input("Masukkan bilangan kedua: "))
if pilihan == '1':
   print(angka_pertama,"+",angka_kedua,"=", penjumlahan(angka_pertama,angka_kedua))
elif pilihan == '2':
   print(angka_pertama,"-",angka_kedua,"=", pengurangan(angka_pertama,angka_kedua))
elif pilihan == '3':
   print(angka_pertama,"*",angka_kedua,"=", perkalian(angka_pertama,angka_kedua))
elif pilihan == '4':
   print(angka_pertama,"/",angka_kedua,"=", pembagian(angka_pertama,angka_kedua))