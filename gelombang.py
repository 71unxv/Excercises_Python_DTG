import numpy as np
import matplotlib.pyplot as plt
t = np.linspace (0,10,100)
A = 10
f = 50
w = 2*3.14*f

y = A * np.exp(t*-1)*np.sin(w*t)
plt.plot(t,y)
