import numpy as np
import matplotlib.pyplot as plt

t= np.linspace(0,10,500)
n=np.linspace(0,10,100)
value = len(t)//4
value_n = len(n)//4
impulse=np.zeros(len(t))
impulse[2*value]= 1
impulse_n=np.zeros(len(n))
impulse_n[2*value_n]= 1

fig,a=plt.subplots(2,1)
a[0].plot(t,impulse)
a[0].set_xlabel("time")
a[0].set_ylabel("amplitude")
a[1].stem(n,impulse_n)
a[1].set_xlabel("time")
a[1].set_ylabel("amplitude")
plt.tight_layout()
plt.show()