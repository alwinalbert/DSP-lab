import numpy as np
import matplotlib.pyplot as plt
t= np.linspace(-10,10,1000)
value = len(t)//4
sine_t = np.sin(t)
rect_t = np.concatenate((np.zeros(value),np.ones(value),np.ones(value),np.zeros(value)))
result = sine_t*rect_t
plt.plot(t,result)
plt.xlabel("time")
plt.ylabel("amplitude")
plt.show()