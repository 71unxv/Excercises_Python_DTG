# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 12:56:47 2019

@author: Almarsa
"""

import numpy as np
import JIMT1Dinv.MTobj as mt
import matplotlib.pyplot as plt
import pickle
import pandas as pd
import scipy.interpolate as sci

#def read(filename):
#    with open(filename, 'rb') as inputdata:
#        hasilread = pickle.load(inputdata)
#    return hasilread
##    
#data = mt.ModelMT.read('dataDummy.MT')

Topo = pd.read_csv('Book1ia.csv',names=['x','y','z'])
#print(Topo)
#
#plt.scatter(Topo.x, Topo.y, c=Topo.z)
#plt.show()

Xmin,Xmax = Topo.x.min(), Topo.x.max()
Ymin,Ymax = Topo.y.min(), Topo.y.max()

Xgrid,Ygrid = np.meshgrid(np.linspace(Xmin,Xmax,50), np.linspace(Ymin,Ymax,50))
fungsiinter = sci.Rbf(Topo.x, Topo.y, Topo.z)
Zgrid = fungsiinter(Xgrid,Ygrid)

plt.figure(figsize=(15,15))
extend = (Xmin, Xmax, Ymin, Ymax)
plt.contourf(Zgrid,extent = extend)
cb = plt.scatter(Topo.x, Topo.y, s=21, c=Topo.z, edgecolor='#ffffff66')
plt.colorbar(cb, shrink=0.67)
plt.xlabel("easting")
plt.ylabel("northing")
plt.title("Nilai Pengukuran")
plt.show()

