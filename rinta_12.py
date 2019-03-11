# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 14:15:53 2019

@author: RINTA
"""

import numpy as np
import matplotlib.pyplot as plt
import pickle
import pandas as pd
import scipy.interpolate as scInt

Topo = pd.read_csv('topo_utm_last.csv',names=['x','y','z'])

plt.scatter(Topo.x,Topo.y,c=Topo.z)
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.title('Titik Pengukuran')
plt.show()      #Klo di run dgn terminal gabisa muncul klo ga pake ini
N=50
Xmin,Xmax = Topo.x.min(),Topo.x.max()
Ymin,Ymax = Topo.y.min(),Topo.y.max()
X = np.linspace(Xmin,Xmax,N)
Y = np.linspace(Ymin,Ymax,N)
XX,YY=np.meshgrid(X,Y)

fig2=plt.plot(XX,YY,('k.'))
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.title('Titik Interpolasi')
plt.show()

f_interp=scInt.Rbf(Topo.x, Topo.y, Topo.z,smooth = 2)
ZZ = f_interp(XX,YY)

extend = (Xmin,Xmax,Ymin,Ymax)
#plt.imshow(ZZ,extent=extend)
plt.contourf(ZZ,extent=extend)
cb = plt.scatter(Topo.x, Topo.y, s=60, c=Topo.z, edgecolor='#ffffff66')
plt.colorbar(cb, shrink=0.67)
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.title('Hasil Interpolasi')
plt.show()