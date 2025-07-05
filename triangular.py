import numpy as np
import matplotlib.pyplot as plt

t= np.linspace(-10,10,500)
n=np.linspace(-10,10,60)
value = len(t)//4
value_n = len(n)//4
traingular = np.concatenate((-10-t[0:value],t[value:3*value],10-t[3*value:]))
traingular_n = np.concatenate((-10-n[0:value_n],n[value_n:3*value_n],10-n[3*value_n:]))

fig,a=plt.subplots(2,1)
a[0].plot(t,traingular)
a[0].set_xlabel("time")
a[0].set_ylabel("amplitude")
a[1].stem(n,traingular_n)
a[1].set_xlabel("time")
a[1].set_ylabel("amplitude")
plt.show()