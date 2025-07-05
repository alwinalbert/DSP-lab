import numpy as np
import matplotlib.pyplot as plt

t= np.linspace(0,10,500)
n=np.linspace(0,10,100)
exponential = np.exp(t)
exponential_n = np.exp(n)

fig,a=plt.subplots(2,1)
a[0].plot(t,exponential)
a[0].set_xlabel("time")
a[0].set_ylabel("amplitude")
a[1].stem(n,exponential_n)
a[1].set_xlabel("time")
a[1].set_ylabel("amplitude")
plt.show()