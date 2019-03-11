# -*- coding: utf-8 -*-
import numpy as np
import pickle
from JIMT1Dinv.MTfunc import *
import matplotlib as mpl


data = read('dataDummy.MT')
model = read('modelDummy.mod')

fig1 = mpl.pyplot.subplot(221)
mpl.pyplot.loglog(data.Frequency,data.AppRes,'*b')
mpl.pyplot.xlabel('Frequency (Hz)')
mpl.pyplot.ylabel('Apperent Resistivity')
mpl.pyplot.grid()

mpl.pyplot.subplot(223,xscale = "log")
mpl.pyplot.plot(data.Frequency,data.Phase,'*r')
mpl.pyplot.xlabel('Frequency (Hz)')
mpl.pyplot.ylabel('Apperent Phase')
mpl.pyplot.grid()

mpl.pyplot.subplot(122,xscale = "log")
mpl.pyplot.step(model.res,np.cumsum(model.thick))
mpl.pyplot.gca().invert_yaxis()
mpl.pyplot.xlabel('Resistivity (Hz)')
mpl.pyplot.ylabel('Depth')
mpl.pyplot.grid()
