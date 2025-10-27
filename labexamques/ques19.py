import numpy as np
import matplotlib.pyplot as plt
def dft(x):
    N =len(x)
    n = np.arange(N)
    k = n.reshape((N,1))
    w = np.exp(-2j*np.pi*k*n/N)
    X = np.dot(w,x)
    return X

x = np.array([2*(1/4)**n for n in range(6)])
N = int(input("enter dft size: "))
x_pad = np.pad(x,(0,N-len(x)))
x_dtft = dft(x_pad)
plt.plot(x_dtft)
plt.show()

