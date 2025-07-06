import numpy as np
import matplotlib.pyplot as plt
t= np.linspace(-10,10,1000)
result = np.exp(-3*np.abs(t))
plt.plot(t,result)
plt.xlabel("time")
plt.ylabel("amplitude")
plt.show()