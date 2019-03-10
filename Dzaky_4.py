# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 15:25:18 2019

@author: gayuh
"""

# taking input from user
number=[]
# prime number is always greater than 1
for i in range(1,20):
    number.append(i)
for i in number:
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                print(number, "is not a prime number")
                break
            else:
                print(number, "is a prime number")

# if the entered number is less than or equal to 1
# then it is not prime number
    else:
        print(number, "is not a prime number")
