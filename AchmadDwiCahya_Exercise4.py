def PrintPrime(A):
    for number in A:
        isi = 0
        for i in range(1,number+1):
            if number % i == 0:
                isi += 1
        if isi == 2:
            print('Bilangan Prima')
        elif isi == 2:
            print('Bilangan Prima')
        else:
            print('Bukan Bilangan Prima')
        isi = 0
        

PrintPrime([1,2,3,4,5,6,7,8,9,10])