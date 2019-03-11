# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 12:01:18 2019

@author: RINTA
"""
import numpy as np
import matplotlib.pyplot as plt
import pickle

def read(FileName):
    with open(FileName,'rb') as inputdata :
        hasilread = pickle.load(inputdata)
        return hasilread


data = read('dataDummy.MT')

grid = plt.GridSpec(2, 2, wspace=0.6, hspace=7)

fig=plt.figure()
fig1=plt.subplot(2,2,1)
fig1.loglog(data.Frequency,data.AppRes,'.r')
plt.xlabel('Frequency')
plt.ylabel('Phase')
plt.grid()

fig2=plt.subplot(2,2,3)
fig2.loglog(data.Frequency,data.Phase,'.r')
plt.ylabel('AppRes')
plt.xlabel('Frequency')
plt.grid()

Model = read('modelDummy.mod')
cumThick=np.cumsum(Model.thick)
fig3=plt.subplot(grid[0:,1])
fig3.step(Model.res,cumThick)
plt.title('1D Resistivity Profile')
plt.ylabel('Depth (m)')
plt.xlabel('Resistivity (Ohm.m)')
plt.gca().invert_yaxis()
plt.grid()
plt.xticks(np.logspace(0.01,1000,1000))
plt.xscale('log')