import numpy as np
import matplotlib.pyplot as plt

def dft(x):
    N = len(x)
    y = np.zeros(N, dtype=complex)
    for k in range(N):
        for n in range(N):
            y[k] += x[n] * np.exp(-2j * np.pi * k * n / N)
    return y

def circular_convolution(x, h):
    lhs = np.fft.ifft(np.fft.fft(x) * np.fft.fft(h))
    rhs = np.fft.ifft(dft(x)*dft(h))
    return lhs, rhs
   
x = np.array(eval(input("Enter a list of numbers: ")),dtype = complex)
h = np.array(eval(input("Enter a list of numbers: ")),dtype = complex)
lhs,rhs = circular_convolution(x, h)
print("Left-hand side (using FFT):", lhs)
print("Right-hand side (using DFT):", rhs)
plt.subplot(2,2,1)
plt.stem(np.abs(lhs))
plt.title("Magnitude of LHS (FFT)")
plt.subplot(2,2,2)
plt.stem(np.abs(rhs))
plt.title("Magnitude of RHS (DFT)")
plt.subplot(2,2,3)
plt.stem(np.angle(lhs))
plt.title("Phase of LHS (FFT)")
plt.subplot(2,2,4)
plt.stem(np.angle(rhs))
plt.title("Phase of RHS (DFT)")
plt.tight_layout()
plt.show()