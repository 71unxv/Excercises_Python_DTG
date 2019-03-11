# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 13:12:50 2019

@author: ASUS
"""

putri, lia, adjeng = 'Putriyu', 'Liayu', 'Adjengyu'
have, andthepriceis = 'have', 'and the price is'
apple = 'apple'
appleputri, applelia, appleadjeng = 8, 6, 12
priceputri, pricelia, priceadjeng = 100.00, 75.00, 150.00
appleprice = 12.50

print(putri+f'{appleputri}'+apple+andthepriceis+f'{priceputri}')
print(lia+f'{applelia}'+apple+andthepriceis+f'{pricelia}')
print(adjeng+f'{appleadjeng}'+apple+andthepriceis+f'{priceadjeng}') 
print('and the price is for 1'+ f'{appleprice}' + 'is' + f'{apple}')