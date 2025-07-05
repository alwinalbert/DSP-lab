import numpy as np
import matplotlib.pyplot as plt
f = 1
t= np.linspace(0,10,500)
n=np.linspace(0,10,100)
sine = np.sin(2*np.pi*f*t)
sine_n = np.sin(2*np.pi*f*n)
fig,a=plt.subplots(2,1)
a[0].plot(t,sine)
a[0].set_xlabel("time")
a[0].set_ylabel("amplitude")
a[1].stem(n,sine_n)
a[1].set_xlabel("time")
a[1].set_ylabel("amplitude")
plt.show()