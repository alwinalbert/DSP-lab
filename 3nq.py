import numpy as np
import matplotlib.pyplot as plt

def impulse(x,x0=0):
    return np.where(x==x0,1,0)

def x(n):
    result = np.zeros_like(n)
    result += 2*impulse(n+1) + 3*impulse(n) + 2*impulse(n-1) + impulse(n-2)
    return result

n = np.arange(-10,11,1)

plt.title("x(3n+2)")
plt.xlabel("time")
plt.ylabel("amplitude")
plt.stem(n,x(-3*n+2))
plt.show()
