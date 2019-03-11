# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 11:49:26 2019

@author: Almarsa
"""

import pickle
def read(filename):
    with open(filename, 'rb') as inputdata:
        hasilread = pickle.load(inputdata)
        return hasilread
    
data = read ('dataDummy.MT')

