import numpy as np
import matplotlib.pyplot as plt

def  dft(x):
    N =len(x)
    X =[0]*N
    for k in range (N):
        for n in range(N):
            X[k] += x[n]*np.exp(-2j*np.pi*k*n/N)
    return np.array(X)

def idft(X):
    N =len(X)
    x = [0]*N
    for n in range(N):
        for k in range(N):
            x[n]+= (1/N)* X[k]*np.exp(2j*np.pi*k*n/N)
    return np.array(x)

def circular_conv(x,h):
    N =len(x)
    z = [0]*N
    for n in range(N):
        for k in range(N):
            z[n] += x[k] * h[(n-k)% N]
    return np.array(z)

x = np.array(eval(input("enter the elements x: ")),dtype=complex)
h = np.array(eval(input("enter the elements h: ")),dtype=complex)
z = circular_conv(x,h)
X = dft(x)
H = dft(h)
Z = X * H
y = idft(Z)
print("product of DFTs: ",Z)
print("circular convolution output: ",z)
print("IDFT of product of DFTs: ",y)
plt.subplot(2,1,1)
plt.stem(np.abs(z))
plt.title("circular convolution output")
plt.subplot(2,1,2)
plt.stem(np.abs(y))
plt.title("IDFT of product of DFTs")
plt.tight_layout()
plt.show()
