# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 17:18:30 2019

@author: redof
"""
class Calc():

   @staticmethod
   def add(x, y):
       return x + y

   @staticmethod
   def div(x, y):
       return x / y

   @staticmethod
   def get_numbers():
       num1 = int(input("Enter first number: "))
       num2 = int(input("Enter second number: "))
       return num1, num2

   @staticmethod
   def get_operator():
       operator = input('Please enter an operator (+, -, *, /): ')
   return operator

   @classmethod
   def calculate(cls):
       num1, num2 = cls.get_numbers()
       operator = cls.get_operator()
        if operator == '+':
            print (cls.add(num1, num2))
        elif operator == '-':
            print (cls.sub(num1, num2))
        elif operator == '*':
            print (cls.mul(num1, num2))
        elif operator == '/':
            print (cls.div(num1, num2))


    Calc.calculate()