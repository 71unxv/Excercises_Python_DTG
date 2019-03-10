#KALKULATOR REDO

class Calculator():
    def Perkalian(x,y):
        return x * y
    def Pembagian(x,y):
        return x / y
    def Penjumlahan(x,y):
        return x + y
    def Pengurangan(x,y):
        return x - y  
    
    print('KALKULATOR')
    print('-----------')
    print('1. Perkalian')
    print('2. Pembagian')
    print('3. Penjumlahan')
    print('4. Pengurangan')
    
    pilihan = input("Pilih operasi matematis :")
    
    num1 = int(input("Masukkan angka pertama :"))
    num2 = int(input("Masukkan angka kedua :"))
    
    if pilihan == '1':
        print(num1,"*",num2,"=", num1 * num2)
        
    elif pilihan == '2':
        print(num1,"/",num2,"=", num1 / num2)
            
    elif pilihan == '3':
        print(num1,"+",num2,"=", num1 + num2)
                
    elif pilihan == '4':
        print(num1,"-",num2,"=", num1 - num2)
    else:
        print("ERROR BROHHH")



