import numpy as np
import matplotlib.pyplot as plt

def dft(x):
    N =len(x)
    X = [0]*N
    for k in range(N):
        for n in range(N):
            X[k]+=x[n]*np.exp(-2j*np.pi*k*n/N)
    return np.array(X)

x =np.array(eval(input("enter the elements: "))) 
x_dft = dft(x)
N = len(x)
#x_shifted = np.roll(x,-2)
#x_shifted_dft  = dft(x_shifted)
x_lin_shift = np.concatenate(([0,0],x))[:N]
x_shifted_dft  = dft(x_lin_shift)
plt.subplot(2,2,1)
plt.stem(np.abs(x_dft))
plt.title("Magnitude of DFT of original signal")
plt.subplot(2,2,2)
plt.stem(np.abs(x_shifted_dft))
plt.title("Magnitude of DFT of shifted signal using np.roll")
plt.subplot(2,2,3)
plt.stem(np.angle(x_shifted_dft))
plt.title("Phase of DFT of shifted signal using np.roll")
plt.subplot(2,2,4)
plt.stem(np.angle(x_dft))
plt.title("Phase of DFT of original signal")
plt.tight_layout()
plt.show()
