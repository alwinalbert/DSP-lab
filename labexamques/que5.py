import numpy as np
import matplotlib.pyplot as plt

def dft(x):
    X =[]
    N =len(x)
    for k in range(N):
        s=0
        for n in range(N):
            s+=x[n]*np.exp(-2j*np.pi*k*n/N)
        X.append(s)
    return np.array(X)

def idft(X):
    N=len(X)
    x_t = []
    for n in range(N):
        s =0
        for k in range(N):
            s += (1/N) * X[k] * np.exp(2j*np.pi*k*n/N)
        x_t.append(s)
    return np.array(x_t)

def circular_conv(x1,x2):
    N = len(x1)
    z = np.zeros(N)
    for n in range(N):
        for m in range(N):
            z[n] += x1[m] * x2[ (n-m) % N ]
    return z

x1_og=np.array([1,2,3])
x2_og=np.array([2,3])
x1= np.zeros(5)
x2 = np.zeros(5)
x1[:len(x1_og)] = x1_og
x2[:len(x2_og)] = x2_og

X1_dft = dft(x1)
X2_dft = dft(x2)
y = X1_dft*X2_dft
z= circular_conv(x1,x2)
w = idft(y)
plt.subplot(2,2,1)
plt.stem(z)
plt.xlabel('n') 
plt.ylabel('Amplitude')
plt.title('Circular Convolution of x1(n) and x2(n)')
plt.subplot(2,2,2)
plt.stem(np.abs(w))
plt.xlabel('n')
plt.ylabel('Magnitude')
plt.title('Magnitude of IDFT of the product')
plt.tight_layout()
plt.show()