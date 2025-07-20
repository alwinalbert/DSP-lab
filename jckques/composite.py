
import numpy as np
import matplotlib.pyplot as plt
t= np.linspace(0,10,1000)
result = 10*np.cos(3140*t)+5*np.sin(6280*t)
plt.plot(t,result)
plt.xlabel("time")
plt.ylabel("amplitude")
plt.show()
