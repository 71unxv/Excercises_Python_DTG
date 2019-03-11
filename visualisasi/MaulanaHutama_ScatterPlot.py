# -*- coding: utf-8 -*-
# =============================================================================
# SCATTER PLOT AND GRIDDING
# =============================================================================
import pandas as pd
import matplotlib.pyplot as plt
#import matplotlib as mtplt
import numpy as np
import scipy.interpolate as scpyInterp

Topo = pd.read_csv('maul.csv', names = ['x','y','z'])

plt.scatter(Topo.x, Topo.y, Topo.z)
plt.show()

Xmin,Xmax = Topo.x.min(),Topo.x.max()
Ymin,Ymax = Topo.y.min(),Topo.y.max()

Xgrid,Ygrid = np.mgrid[Xmin:Xmax:100j,Ymin:Ymax:100j]
plt.plot(Xgrid,Ygrid)
plt.show()


maul = scpyInterp.Rbf(Topo.x, Topo.y, Topo.z,smooth = 1)
Zgrid = maul(Xgrid,Ygrid)

#plt.figure(figsize=(10, 10))
extend = (Xmin, Xmax, Ymin, Ymax)
plt.contourf(Zgrid.T, extent = extend)
plt.xlabel('Easting (m)')
plt.ylabel('Northing (m)')
plt.colorbar()
#plt.imshow(Zgrid)

cb = plt.scatter(Topo.x, Topo.y, s=60, c=Topo.z, edgecolor='#ffffff66')
#plt.show()