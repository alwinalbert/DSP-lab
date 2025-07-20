import numpy as np
import matplotlib.pyplot as plt

t= np.linspace(0,10,500)
n=np.linspace(0,10,100)
value = len(t)//4
value_n = len(n)//4
bipolar = np.concatenate((np.zeros(value),np.ones(value),-np.ones(value),np.zeros(value)))
bipolar_n = np.concatenate((np.zeros(value_n),np.ones(value_n),-np.ones(value_n),np.zeros(value_n)))

fig,a=plt.subplots(2,1)
a[0].plot(t,bipolar)
a[0].set_xlabel("time")
a[0].set_ylabel("amplitude")
a[1].stem(n,bipolar_n)
a[1].set_xlabel("time")
a[1].set_ylabel("amplitude")
plt.show()