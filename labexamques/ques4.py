import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(0,1,1000)
xa = np.cos(20*np.pi*t)

def dft(x):
    X = []
    N = len(x)
    for k in range(N):
        s =0
        for n in range(N):
            s+=x[n]*np.exp(-2j*np.pi*k*n/N)
        X.append(s)
    return np.array(X)

def idft(x):
    N = len(x)
    x_t = []
    for n in range(N):
        s =0 
        for k in range(N):
            s += (1/N)*x[k]*np.exp(-1j*2*np.pi*k*n/N)
        x_t.append(s)
    return np.array(x_t)

Ts1 = 0.01
fs1 = 1/Ts1
N1 = int(1/Ts1)
n1 = np.arange(N1)
t1 = n1*Ts1
x1 = np.cos(20*np.pi*t1)

x1_dft = dft(x1)
x1_idft = idft(x1_dft)

Ts2 = 0.05
fs2 = 1/Ts2
N2 = int(1/Ts2)
n2 = np.arange(N2)
t2 = n2*Ts2
x2 = np.cos(20*np.pi*t2)
x2_dft = dft(x2)
x2_idft = idft(x2_dft)

Ts3 = 0.1
fs3 = 1/Ts3
N3 = int(1/Ts3)
n3 = np.arange(N3)
t3 = n3*Ts3
x3 = np.cos(20*np.pi*t3)
x3_dft = dft(x3)
x3_idft = idft(x3_dft)

plt.figure(figsize=(12,12))
plt.subplot(3,2,1)
plt.stem(n1,x1)
plt.title('x1[n] with Ts=0.01')
plt.subplot(3,2,2)
plt.stem(np.abs(x1_dft))
plt.title('Magnitude of DFT of x1[n]')
plt.subplot(3,2,3)
plt.stem(n2,x2)
plt.title('x2[n] with Ts=0.05')
plt.subplot(3,2,4)
plt.stem(np.abs(x2_dft))
plt.title('Magnitude of DFT of x2[n]')
plt.subplot(3,2,5)
plt.stem(n3,x3)
plt.title('x3[n] with Ts=0.1')
plt.subplot(3,2,6)
plt.stem(np.abs(x3_dft))
plt.title('Magnitude of DFT of x3[n]')
plt.tight_layout()
plt.show()

