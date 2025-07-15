import numpy as np
import matplotlib.pyplot as plt

def impulse(x,x0=0):
    return np.where(x==x0,1,0)

n= np.arange(-10,11,1)
result = np.zeros_like(n)
for k in range(4):
    result += impulse(n-k)

plt.title("summation")
plt.xlabel("time")
plt.ylabel("amplitude")
plt.stem(n,result)
plt.show()    



