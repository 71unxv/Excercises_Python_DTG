# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 14:06:34 2019

@author: redof
"""
import numpy as np
import pandas as pd
import matplotlib as mtplot
import matplotlib.pyplot as plt
import scipy.interpolate as scpyInterp

Topo = pd.read_csv('topoSBY.csv',names=['x','y','z'])

# plt.plot(Topo['x'],Topo['y'],('k.'))
plt.scatter(Topo.x, Topo.y, c=Topo.z)
plt.colorbar(cb, shrink=1)
plt.show()
plt.grid()

#kedua
Xmin,Xmax = Topo['x'].min(),Topo['x'].max()
Ymin,Ymax = Topo['y'].min(),Topo['y'].max()

Xgrid,Ygrid = np.meshgrid(np.linspace(Xmin,Xmax,50),np.linspace(Ymin,Ymax,50))
Xgrid, Ygrid = np.mgrid[Xmin:Xmax:500,Ymin:Ymax:500]

#print(type(Xgrid))
plt.plot(Xgrid,Ygrid,('k.'))
plt.show()
plt.figure(figsize=(15,15))

fungsiInterpolasi = scpyInterp.Rbf(Topo.x, Topo.y, Topo.z,smooth = 10)
Zgrid = fungsiInterpolasi(Xgrid, Ygrid)
# print(Xgrid)

plt.figure(figsize=(7,7))
extend = (Xmin, Xmax, Ymin, Ymax)
plt.title('MT DATA CONTOUR')

plt.contourf(Zgrid.T,extent = extend)

#cb = plt.scatter(Topo.x, Topo.y, s=60, c=Topo.z, edgecolor='#ffffff66')
plt.colorbar(cb, shrink=1)
plt.show()



