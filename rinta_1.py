# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 12:55:16 2019

@author: RINTA
"""

jhon, dilan, sarah = 'Jhon have ', 'Dilan have ', 'Sarah have '
have, andthepriceis = 'have', 'and the price is '
apple = ' apple '
ap_jhon, ap_dilan, ap_sarah = 8, 6, 12
price_jhon, price_dilan, price_sarah = 100.00, 75.00, 150.00
ap = 12.50

print(jhon+f'{ap_jhon}'+apple+andthepriceis+f'{price_jhon}')
print(dilan+f'{ap_jhon}'+apple+andthepriceis+f'{price_dilan}')
print(sarah+f'{ap_jhon}'+apple+andthepriceis+f'{price_dilan}')
print('and the price for 1 '+ apple+ ' is '+ f'{ap}')