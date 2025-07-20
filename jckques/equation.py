import numpy as np
import matplotlib.pyplot as plt
n = np.arange(-10,11,1)
def u(n):
    return np.where(n>=0,1,0)

def x(n):
    return (-1.0)**n * 2.0**n * (u(n)-u(n-5))

result = x(n-2) + x(n+3)

plt.title("equation question")
plt.xlabel("time")
plt.ylabel("amplitude")
plt.stem(n,result)
plt.grid(True)
plt.show()






