import numpy as np
import matplotlib.pyplot as plt

t= np.linspace(0,10,500)
n=np.linspace(0,10,100)
ramp = t
ramp_n=n
fig,a=plt.subplots(2,1)
a[0].plot(t,ramp)
a[0].set_xlabel("time")
a[0].set_ylabel("amplitude")
a[1].stem(n,ramp_n)
a[1].set_xlabel("time")
a[1].set_ylabel("amplitude")
plt.tight_layout()
plt.show()