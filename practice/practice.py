"""import numpy as np
import matplotlib.pyplot as plt
def dft(x):
    N = len(x)
    X = []
    for k in range(N):
        s =0 
        for n in range(N):
            s += x[n]*np.exp(-2j*np.pi*k*n/N)
        X.append(s)
    return np.array(X)

x = np.array(eval(input("enter the elements: ")),dtype=complex)
shift = int(input("enter the shift: "))
N =len(x)
k = np.arange(N)
x_shifted = np.roll(x,shift)
z = dft(x_shifted)
lhs = z
w = dft(x)
phase=np.exp(-2j*np.pi*k*shift/N)
rhs = w *phase
print("lhs",lhs)
print("rhs",rhs)
plt.subplot(2,2,1)
plt.title('magnitude of lhs')
plt.stem(np.abs(lhs))
plt.subplot(2,2,2)
plt.title('magnitude of rhs')
plt.stem(np.abs(rhs))
plt.tight_layout()
plt.show()"""

""" import numpy as np
import matplotlib.pyplot as plt
def dft(x):
    N = len(x)
    X = []
    for k in range(N):
        s =0 
        for n in range(N):
            s += x[n]*np.exp(-2j*np.pi*k*n/N)
        X.append(s)
    return np.array(X)
x = np.array([1, 2, 3, 4], dtype=complex)  # Example: replace with your values
shift = 2  # Example shift value
# x = np.array(eval(input("enter the elements: ")),dtype=complex)  # Original line
# shift = int(input("enter the shift: "))  # Original line
N =len(x)
n = np.arange(N)
x_modulated = x*np.exp(2j*np.pi*shift*n/N)
z = dft(x_modulated)
lhs = z
w = dft(x)
rhs = np.roll(w,-shift)
print("lhs",lhs)
print("rhs",rhs)
plt.subplot(2,2,1)
plt.title('magnitude of lhs')
plt.stem(np.abs(lhs))
plt.subplot(2,2,2)
plt.title('magnitude of rhs')
plt.stem(np.abs(rhs))
plt.tight_layout()
plt.show() """

""" import numpy as np
import matplotlib.pyplot as plt
def dft(x):
    N =len(x)
    X = []
    for k in range(N):
        s =0 
        for n in range(N):
            s += x[n]*np.exp(-2j*np.pi*k*n/N)
        X.append(s)
    return np.array(X)

def parsevals(x):
    N = len(x)
    X = dft(x)
    lhs = np.sum(np.abs(x)**2)
    rhs = (1/N)*np.sum(np.abs(X)**2)  
    return lhs, rhs

x = np.array(eval(input("enter the elements: ")),dtype=complex)
lhs,rhs = parsevals(x)
print("lhs",lhs)
print("rhs",rhs)
plt.subplot(2,1,1)
plt.title('lhs value')      
plt.bar([0],lhs)
plt.subplot(2,1,2)
plt.title('rhs value')
plt.bar([0],rhs)
plt.tight_layout()
plt.show() """

import numpy as np
import matplotlib.pyplot as plt
def dft(x):
    N = len(x)
    X = []
    for k in range(N):
        s = 0 
        for n in range(N):
            s += x[n]*np.exp(-2j*np.pi*k*n/N)
        X.append(s)
    return np.array(X)
def circular_convolution(x,h):
    N = len(x)
    z  = [0]*N
    for n in range(N):
        for k in range(N):
            z[n]+=x[k]*h[(n-k) % N]
    return np.array(z)

x = np.array(eval(input("enter the elements x: ")))
h = np.array(eval(input("enter the elements h: ")))
N = len(x)
lhs = dft(x*h)
rhs = (1/N)*circular_convolution(dft(x),dft(h))
print("lhs",lhs)
print("rhs",rhs)
plt.subplot(2,2,1)
plt.title('magnitude of lhs')
plt.stem(np.abs(lhs))
plt.subplot(2,2,2)
plt.title('magnitude of rhs')
plt.stem(np.abs(rhs))
plt.tight_layout()
plt.show()

"""import numpy as np
import matplotlib.pyplot as plt

def dft(x):
    N =len(x)
    X = [0]*N
    for k in range(N):
        for n in range(N):
            X[k] += x[n]*np.exp(-2j*np.pi*k*n/N)
    return np.array(X)

def idft(X):
    N = len(X)
    x = [0]*N
    for n in range(N):
        for k in range (N):
            x[n] += (1/N)*X[k]*np.exp(2j*np.pi*k*n/N)
    return np.array(x)

x = np.array(eval(input("enter the elements: ")),dtype=complex)
X = dft(x)
x_reconstructed = idft(X)
print("Reconstructed x[n]: ", x_reconstructed)
plt.subplot(3,1,1)
plt.title('Original x[n]')
plt.stem(np.abs(x))
plt.subplot(3,1,2)
plt.title('DFT Magnitude')
plt.stem(np.abs(X)) 
plt.subplot(3,1,3)
plt.title('Reconstructed x[n]')
plt.stem(np.abs(x_reconstructed))
plt.tight_layout()
plt.show()"""

"""import numpy as np
import matplotlib.pyplot as plt

def dit_fft(x):
    N =len(x)
    if N ==1:
        return x
    if np.log2(N)%1 != 0:
        print("enter the length of x as power of 2 completed")
        return
    X_even = x[0::2]
    X_odd = x[1::2]
    X_e = dit_fft(X_even)
    X_o = dit_fft(X_odd)
    twiddle = np.exp(-2j*np.pi*np.arange(N)/N)
    return np.concatenate([
        X_e + twiddle[:N//2]* X_o,
        X_e - twiddle[:N//2]*X_o
        ])

x = np.array(eval(input("enter x[n] should be length of power of 2:")))
x_fft = dit_fft(x)
x_fft_numpy = np.fft.fft(x)
print("FFT using numpy is: ", x_fft_numpy)
plt.subplot(2,1,1)
plt.stem(np.abs(x_fft_numpy))
plt.title("FFT Output using Numpy")
plt.subplot(2,1,2)
plt.stem(np.abs(x_fft))
plt.title("FFT Output using DIT-FFT Algorithm")
plt.xlabel("k")
plt.tight_layout()
plt.show()
"""


