import numpy as np
import matplotlib.pyplot as plt
t= np.linspace(-10,10,1000)
sinc_t=np.sin(np.pi*t)/t
plt.plot(t,sinc_t)
plt.xlabel("time")
plt.ylabel("amplitude")
plt.show()