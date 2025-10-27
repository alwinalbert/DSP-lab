import numpy as np
import matplotlib.pyplot as plt

def dft(x):
    N =len(x)
    X = [0]*N
    for k in range(N):
        for n in range(N):
            X[k] += x[n]*np.exp(-2j*np.pi*k*n/N)

    return np.array(X)

f = 10
fs = 50
N = 50
n = np.arange(N)
x = np.sin(2*np.pi*f*n/fs)
X = dft(x)
plt.subplot(3,1,1)
plt.plot(n,x)
plt.title('Input Signal x(n)')
plt.subplot(3,1,2)
freq = np.arange(N)* fs/N
plt.stem(freq,np.abs(X))
plt.title('Magnitude of DFT of x(n)')
plt.subplot(3,1,3)
plt.stem(freq,np.angle(X))
plt.title('Phase of DFT of x(n)')
plt.tight_layout()
plt.show()