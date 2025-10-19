import numpy as np
import matplotlib.pyplot as plt

def dft(x):
    N=len(x)
    X =[]
    for k in range(N):
        s=0
        for n in range(N):
            s+=x[n]*np.exp(-2j*np.pi*k*n/N)
        X.append(s)
    return np.array(X)

f = 5
fs = 50
N=50
n = np.arange(N)
x = np.sin(2*np.pi*f*n/fs)
plt.subplot(3,1,1)
plt.stem(n,x)
plt.title('Input Signal x(n)')
X_dft = dft(x)
plt.subplot(3,1,2)
plt.stem(np.abs(X_dft))
plt.title('Magnitude of DFT of x(n)')
plt.subplot(3,1,3)
plt.stem(np.angle(X_dft))
plt.title('Phase of DFT of x(n)')
plt.tight_layout()
plt.show()
