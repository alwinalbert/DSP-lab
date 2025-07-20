import numpy as np  
import matplotlib.pyplot as plt

n = np.arange(-10,11,1)

def u(n):
    return np.where(n>=0,1,0)

result = u(n) - u(n-1)

plt.title("impulse fn from u(n) - u(n-1)")
plt.xlabel("time")
plt.ylabel("amplitude")
plt.stem(n,result)
plt.grid(True)
plt.show()
